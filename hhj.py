print("citybusQ8")

print(""""
 A project that helps people in booking and makes it easier for 
      The company organization and management as it provides the company with statistics and 
      Help her to know the profits and know every small and big in 
      Organizing and booking and helps people book quickly without 
      Waiting and helps them know the prices and benefit from the offers
""")

agt = input("What is your name: ")
print(f"Welcome to citybusQ8 {agt}")

akk = input("How old are you?")

allf = input("Where country is it from?")

att = input(f"Hello {agt} There are flights to the following places: (kerwan - Salmiya - Doha): ")

def citybusQ8(Flights):
    if Flights == "kerwan":
        return 30 
    if Flights == "Salmiya":
        return 40
    if Flights == "Doha":
        return 35
    else:
        print("The flight does not exist")

citybusQ8(att)

print(f"""
Your Bill 
Name : {agt}
lifetim : {akk}
country : {allf}
city : {citybusQ8(att)}


""")