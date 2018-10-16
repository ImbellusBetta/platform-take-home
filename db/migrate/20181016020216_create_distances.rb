class CreateDistances < ActiveRecord::Migration[5.0]
  def change
    create_table :distances do |t|
      t.integer :location_one_id
      t.integer :location_two_id
      t.decimal :miles

      t.timestamps
    end
  end
end
