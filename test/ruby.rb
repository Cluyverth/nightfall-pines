require 'net/http'
require 'json'

class WeatherFetcher
  API_URL = 'https://api.weatherapi.com/v1/current.json'

  def initialize(api_key)
    @api_key = api_key
  end

  def fetch(city)
    uri = URI("#{API_URL}?key=#{@api_key}&q=#{city}")
    response = Net::HTTP.get(uri)
    JSON.parse(response)
  end
end

weather = WeatherFetcher.new('your_api_key')
puts weather.fetch('Tokyo')
