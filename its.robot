*** Settings ***
Library    RickAndMorty.py
Library    OpenStreetMap.py
Library    OperatingSystem
Library    RequestsLibrary
Variables    variables.py

*** Variables ***

*** Test Cases ***
Count character
    [Documentation]    Сравнение ожидаемого и текущего кол-ва персонажей
    ${count} =  get_character_count
    Should Be Equal  ${count}  ${826}

Coordinates to Addresses
    [Documentation]    Обратное геокодирование
    ${addresses_list_from_coordinates} =  get_addresses_from_coodrinates
    ${addresses_list} =  Get File  addresses.txt
    Should Be Equal As Strings  ${addresses_list_from_coordinates}  ${addresses_list}

Addresses to coordinates
    [Documentation]    Геокодирование
    ${coordinates_list_from_addresses} =  get_coordinates_from_adddreses
    ${coordinates_list} =  Get File  coordinates.txt
    Should Be Equal As Strings  ${coordinates_list_from_addresses}  ${coordinates_list}

Test HTTP Request with Mock
    [Documentation]    HTTP запрос с помощью MOCK
    Create Session    rickandmortyapi    https://rickandmortyapi.com/api    verify=${true}
    ${response}=    GET On Session    rickandmortyapi    /character/123
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json()}    ${mock_response}