class CreateLocations < ActiveRecord::Migration[5.0]
  def change
    create_table :locations do |t|
      t.string :lat_long
      t.string :address
      t.string :query

      t.timestamps
    end
  end
end
