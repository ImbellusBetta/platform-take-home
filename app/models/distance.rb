class Distance < ApplicationRecord
  belongs_to :location_one, class_name: 'Location'
  belongs_to :location_two, class_name: 'Location'

  def calculate
    loc_one = Geokit::Geocoders::GoogleGeocoder.geocode(location_one.lat_long)
    loc_two = Geokit::Geocoders::GoogleGeocoder.geocode(location_two.lat_long)
    self.miles = loc_one.distance_to(loc_two)
    self.save
  end

  def description
    "#{location_one.address} to #{location_two.address} is #{miles.round(2)} miles"
  end
end
