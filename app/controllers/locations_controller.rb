class LocationsController < ApplicationController
  before_action :set_location, only: [:lat_long, :address]

  def show
  end

  def lat_long
    if @location.nil?
      @location = Location.new(query)
      @location.find_address_and_lat_lon(location_params[:address])

      if !@location || !@location.calculate(:ll)
        flash[:danger] = Location.error_message
        redirect_to root_path; return
      end
    end

    flash[:success] = @location.display_lat_long
    redirect_to root_path
  end

  def address
    if @location.nil?
      @location = Location.new(query)
      @location.find_address_and_lat_lon(location_params[:lat_long])

      if !@location || !@location.calculate(:full_address)
        flash[:danger] = Location.error_message
        redirect_to root_path; return
      end
    end

    flash[:success] = @location.display_address
    redirect_to root_path
  end

  private

  def location_params
    params.require(:location).permit(:address, :lat_long)
  end

  def set_location
    @location = Location.find_by(query)
    @location ||= Location.find_by(location_params)
  end

  def query
    {query: (location_params[:address] || location_params[:lat_long])}
  end
end
