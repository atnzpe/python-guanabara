'''
Todos os caminhos levam a Roma

Você receberá uma lista com várias conexões aéreas na Europa. 

Cada conexão é representada como uma tupla com os seguintes elementos:

(cidade_de, cidade_até, hora)

Por exemplo, a tupla a seguir representa um voo de Amsterdã para Dublin que leva 100 minutos:

('Amsterdã', 'Dublin', 100)

Sua tarefa é percorrer todas as rotas em um loop e verificar quantas delas levam a Roma (ou seja, quantas delas têm city_to igual a 'Roma'). Entre as rotas para Roma, você também deve calcular o tempo médio de voo. Imprima a seguinte saída:

{} conexões levam a Roma com um tempo médio de voo de {} minutos

Substitua {} pelo número de conexões e pelo tempo médio de voo.


'''

connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
    
lead_to_rome = 0
time_to_fly = 0

    
for conection in connections:
    if conection[1] == 'Rome':
        
        lead_to_rome += 1
        time_to_fly += conection[2]
        average_flight_time = time_to_fly / lead_to_rome

            
print(f'{lead_to_rome} connections lead to Rome with an average flight time of {average_flight_time:.1f} minutes')