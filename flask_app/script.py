from functions import EmergencyLookup

em = EmergencyLookup('San Francisco')
em.find_site()
print('shelter' in em.scrape_site())
