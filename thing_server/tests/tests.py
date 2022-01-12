import main.py

#Пока не правильный тест



def test_start_game():
    #return gameID and tokenID
    assert start_game({name: 'Inna'}) == {answer: 200, gameID:'00001',
                     '96f98970aa1aee0bc1b085bca99f1737', 
                     playerID: 0, 
                     name:'Inna',}
    
def test_create_game():
    pass


def test_get_tokenID():
    assert get_token({gameID: '00001', name: 'MikeP'}) == {answer: 200, 
                    tokenID:'475dc177afa716b46d041e404890e895', 
                    name: 'MikeP',
                    playerID: 1,}
    
    
#def test_set_name():
#    assert set_name({tokenID:'475dc177afa716b46d041e404890e895', 
#                     name: 'MikeP'}) == {answer:}
    


def test_autotentification():
    assert autotentification ({token: '0001-0001-0001'}) == {answer: True}
    assert autentification ({token: '*'}) == {answer:False}
    assert autentification ({token: '1111'}) == {answer:False}
    

def test_get_cards():
    asset get_cards ({token:'475dc177afa716b46d041e404890e895'}) = {new_carsID: 1}
    
def test_exchange_cards():
    assert exchange_cards {token: 0, 
                           player: 0,
                           cardsID:1}

def test_set_state():
    assert set_state({token: '96f98970aa1aee0bc1b085bca99f1737'}) == 

def test_    
    assert 