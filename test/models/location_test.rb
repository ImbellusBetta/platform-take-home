require 'test_helper'

class LocationTest < ActiveSupport::TestCase
  # Like DistanceTest, most of the work is already tested in their respective gems and are unnnecssary to test.
  # I could test the API, but to not waste calls I'm going to skip that. Note that I could use the VCR gem to hit the API
  # once and save that request, but I was asked to only work on this app for 2-3 hours, so for the sake of that, I'll skip it.
  # However, "block_queries" should be unit tested to make sure it handles all cases.

  test "#Location.block_queries creates a new record when query not previously saved" do
    location_one = '39.099319, -94.582623'
    location_two = '37.7937484,-122.3958389'

    before_location_count = Location.count
    assert Location.count == before_location_count
    Location.block_queries(location_one, location_two)
    assert Location.count == before_location_count + 1
  end

  test "#Location.block_queries returns existing record when query was previously saved" do
    location_one = 'mystringone'
    location_two = 'mystringtwo'

    before_location_count = Location.count
    assert Location.count == before_location_count
    Location.block_queries(location_one, location_two)
    assert Location.count == before_location_count
  end

  test "#Location.block_queries returns existing record when reverse query was previously saved" do
    location_one = 'mystringtwo'
    location_two = 'mystringone'

    before_location_count = Location.count
    assert Location.count == before_location_count
    Location.block_queries(location_one, location_two)
    assert Location.count == before_location_count
  end

  test "#Location.block_queries returns existing record when latlong was previously saved" do
    location_one = 'LatLong1'
    location_two = 'LatLong2'

    before_location_count = Location.count
    assert Location.count == before_location_count
    Location.block_queries(location_one, location_two)
    assert Location.count == before_location_count
  end

  test "#Location.block_queries returns existing record when reverse latlong was previously saved" do
    location_one = 'LatLong2'
    location_two = 'LatLong1'

    before_location_count = Location.count
    assert Location.count == before_location_count
    Location.block_queries(location_one, location_two)
    assert Location.count == before_location_count
  end

  test "#Location.block_queries returns existing record when address was previously saved" do
    location_one = 'Address1'
    location_two = 'Address2'

    before_location_count = Location.count
    assert Location.count == before_location_count
    Location.block_queries(location_one, location_two)
    assert Location.count == before_location_count
  end

  test "#Location.block_queries returns existing record when reverse address was previously saved" do
    location_one = 'Address2'
    location_two = 'Address1'

    before_location_count = Location.count
    assert Location.count == before_location_count
    Location.block_queries(location_one, location_two)
    assert Location.count == before_location_count
  end

  # Tests to make sure the column names haven't changed & not breaking the two description methods
  test 'display_lat_long' do
    location = Location.first
    assert Location.first.display_lat_long == "#{location.address}: #{location.lat_long}"
  end

  test 'display_address' do
    location = Location.first
    assert Location.first.display_address == "#{location.lat_long}: #{location.address}"
  end
end
