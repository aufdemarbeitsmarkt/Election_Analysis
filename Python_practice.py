counties = ["Arapahoe","Denver","Jefferson"]

counties.insert(1, 'El Paso')
counties.remove('Arapahoe')
counties.remove('Denver')
counties.append('Denver')
counties.append('Arapahoe')  

# print(counties)

counties_tuple = ("Arapahoe","Denver","Jefferson")

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

# print(counties_dict)


voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})

voting_data.insert(1, {'county': 'El Paso', 'registered_voters':  461149})

for i,vd in enumerate(voting_data):
    for k,v in vd.items():
        if v == 'Denver':
            voting_data.pop(i)

voting_data.append({"county": "Denver", "registered_voters": 463353})


print(voting_data)