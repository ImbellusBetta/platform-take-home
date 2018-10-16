class Location < ApplicationRecord
  ####
  # Instance Methods
  ####
  def display_lat_long
    "#{address}: #{lat_long}"
  end

  def display_address
    "#{lat_long}: #{address}"
  end

  def calculate(call)
    result =  if call == :ll
                Geokit::Geocoders::GoogleGeocoder.geocode(address)
              else
                Geokit::Geocoders::GoogleGeocoder.geocode(lat_long)
              end

    if result.success?
      if new_record?
        if call == :ll
          self.lat_long = result.ll
        else
          self.address = result.full_address
        end
        self.save
      end
    else
      false
    end
  rescue
    false
  end

  def find_address_and_lat_lon loc
    result = Geokit::Geocoders::GoogleGeocoder.geocode(loc)
    if result.success?
      self.update(lat_long: result.ll, address: result.full_address)
      self
    else
      false
    end
  end

  ####
  # Class methods
  ####
  def Location.calculate_distance params
    location_one = Location.block_queries(params[:location_one], params[:location_two])
    return [ false, Location.error_message ] unless location_one

    location_two = Location.block_queries(params[:location_two], params[:location_one])
    return [ false, Location.error_message ] unless location_two

    distance = Distance.find_or_initialize_by(location_one_id: location_one.id, location_two_id: location_two.id)
    distance.calculate if distance.new_record?

    [ true, distance.description ]
  rescue => e
    [ false, Location.error_message(e) ]
  end

  def Location.block_queries first_location, second_location
    location = Location.find_by(query: first_location)
    location ||= Location.arel_where(first_location)
    location ||= Location.arel_where(second_location) # Reverse in case user decides to switch them around
    location ||= Location.new(query: first_location).find_address_and_lat_lon(first_location)
    location
  end

  def Location.arel_where(loc)
    arel = Location.arel_table
    Location.where(arel[:address].eq(loc).or(arel[:lat_long].eq(loc))).first
  end

  def Location.error_message message="An error occurred"
    "#{message}. Please try again. If it continues to occur, please check your address/lat-long formatting. If that still doesn't, then the internet is broken and you should probably just call it a day."
  end
end
