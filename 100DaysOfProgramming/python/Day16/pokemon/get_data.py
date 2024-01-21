from bs4 import BeautifulSoup as bs
import re

class PokemonInformation:
    def PokemonInformation(html_data):

        with open("/home/caboose/codingProjects/python/udemy/Day16/data/pokemon.web.html") as file:
            PokemonInformation.find_table(file)
            soup = bs(html_data, 'html.parser')
            results = soup.findAll('div')
            for result in results:
                match = get_information(result)
                name = get_name(match)
                number = get_number(match)
                pokemon_type = get_pokemon_type(match)
                

        def get_name(match):
            name = re.findall('', match)
            return name
        
        def get_number(match):
            number = re.findall('', match)
            return number
        

        def get_pokemon_type(match):
            pokemon_type = re.findall('', match)
            return pokemon_type


        def get_information(result):
            
                return re.search( 'infocard ', result.text)

