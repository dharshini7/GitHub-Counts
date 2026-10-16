# import time
#
# from pages.population_page import PopulationPage
#
#
# def test_world_population(driver):
#     # create the population object
#     population_page = PopulationPage(driver)
#     #open the world population page
#     population_page.open_page()
#
#     try:
#         #keep extracting the population continuously
#         while True:
#
#
#         #get the current population
#          population = population_page.get_population()
#         #print population in the terminal
#          print("world population: ", population, flush=True)
#         #wait for a short time before reading again
#          time.sleep(1)
#
#     except KeyboardInterrupt:
#         # this happens whe the user presses ctrl+C
#          print("\nPopulation extration stopped by user.")
#     finally:
#         driver.quit()
#
#



import time
from pages.population_page import PopulationPage

def test_world_population(driver):

    population_page = PopulationPage(driver)
    population_page.open_page()

    try:
        while True:
            population = population_page.get_population()

            print("world population:", population, flush=True)

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nPopulation extraction stopped by user.", flush=True)

    finally:
        print("Closing browser...", flush=True)
        driver.quit()
        print("Browser closed.", flush=True)

