Rails.application.routes.draw do
  resources :locations, only: [:show] do
    collection do
      post 'lat_long'
      post 'address'
    end
  end
  resources :distances, only: [] do
    collection do
      post 'calculate'
    end
  end
  root to: 'locations#show'
end
