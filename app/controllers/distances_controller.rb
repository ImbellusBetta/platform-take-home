class DistancesController < ApplicationController
  def calculate
    @success = false
    message = check_parameters_and_calculate

    if @success
      flash[:success] = message
    else
      flash[:danger] = message
    end
    redirect_to root_path
  end

  private

  def distance_params
    params.require(:distance).permit(:location_one, :location_two)
  end

  def check_parameters_and_calculate
    location_one = distance_params[:location_one]
    location_two = distance_params[:location_two]

    if location_one.blank? && location_two.blank?
      'Locations one & two are missing'
    elsif location_one.blank?
      'Location one is missing'
    elsif location_two.blank?
      'Location two is missing'
    else
      result = Location.calculate_distance(distance_params)
      @success = result[0]
      result[1]
    end
  end
end
