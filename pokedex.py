import requests
class Pokedex:
    def __init__(self, pokemon):
        self.pokemon = pokemon.lower()
        
    def __str__(self):
        return f"""{self.acessa_nome()} 
{self.acessa_id()}
{self.acessa_tipo()}
{self.acessa_altura()}
{self.acessa_peso()}
{self.acessa_habilidade()}"""
        
    def acessa_pokemon(self):    
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon}'
        r = requests.get(url)
        return r.json()
    
    def acessa_nome(self):
        dados = self.acessa_pokemon()
        nome = dados['name']
        return f'Pokemon: {nome.title()}'
        
    def acessa_tipo(self):
        dados = self.acessa_pokemon()
        tipos = dados['types']
        types = []
        for type_dict in tipos:
            type_name = type_dict['type']['name']
            traducao = {
            'fighting': 'lutador',
            'fire': 'fogo',
            'water': 'água',
            'grass': 'grama',
            'flying': 'voador',
            'poison': 'veneno',
            'electric': 'elétrico',
            'ground': 'terra',
            'rock': 'pedra',
            'psychic': 'psíquico',
            'ice': 'gelo',
            'bug': 'inseto',
            'ghost': 'fantasma',
            'steel': 'ferro',
            'dragon': 'dragão',
            'dark': 'sombrio',
            'fairy': 'fada'}
            type_name = traducao[type_name]
            types.append(type_name)
        if len(types) == 1:
            return f'Tipo: {types[0]}'
        else:
            return f'Tipos: {types[0]} e {types[1]}'
            
    def acessa_id(self):
        dados = self.acessa_pokemon()
        pokemon_id = dados['id']
        return f'id: {pokemon_id}'
    
    def acessa_altura(self):
        dados = self.acessa_pokemon()
        altura = dados['height']
        return f'Altura: {altura/10}m'
    
    def acessa_peso(self):
        dados = self.acessa_pokemon()
        peso = dados['weight']
        return f'Peso: {peso/10:.1f}kg'
    
    def acessa_habilidade(self):
        dados = self.acessa_pokemon()
        habilidade = dados['abilities']
        slots = []
        for hability_dict in habilidade:
            hability = hability_dict['ability']['name']
            slots.append(hability)
        if len(slots) == 1:
            return f'Habilidade: {slots[0]}'
        if len(slots) == 2:
            return f'Habilidades: {slots[0]} e {slots[1]}'
        if len(slots) == 3:
            return f'Habilidades: {slots[0]}, {slots[1]} e {slots[2]}'