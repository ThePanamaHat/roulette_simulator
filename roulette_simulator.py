#By ThePanamaHat - email me: thepanamahat (at) pm (dot) me

#To do list:
	
	#Fix so non-intigers don't crash program
	#Calculate the average number of spins before making a profit (started this - commented out)
	#Partial clear at endgame so it leaves the stats with 'c' inputs'
	#Expand options at end game
	#Insert errors for inputs outside of appropriate ranges
		#https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers
	#Graph the results in a GUI
	#Get the simulation to run automatically and test all variables for "bet" to find the optimized bet amount
		#Define optimized bet
	#Include other betting options, such as red/black


#This is to simulate playing roulette in a casino.

#Libraries
import os
import math
import random
import time
import sys
import scipy.stats as st
from progressbar import Bar, Percentage, ProgressBar

#Program loop
while True:

	#Startup screen
	os.system('cls' if os.name == 'nt' else 'clear')
	print('''\n
	  ____             _      _   _                 
	 |  _ \ ___  _   _| | ___| |_| |_ ___           
	 | |_) / _ \| | | | |/ _ \ __| __/ _ \          
	 |  _ < (_) | |_| | |  __/ |_| ||  __/          
	 |_|_\_\___/ \__,_|_|\___|\__|\__\___|          
	 / ___|(_)_ __ ___  _   _| | __ _| |_ ___  _ __ 
	 \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
	  ___) | | | | | | | |_| | | (_| | || (_) | |   
	 |____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   
	 	with statistics, odds, and data analysis...
	''')
	#User input	
	starting_cash = int(input("\nHow much money do you have?: $").replace(',', ''))
	bet = int(input("How much will you be betting per round?: $").replace(',', ''))
	number = int(input('What number will you be betting on? (Choose 1-38; 37=0, 38=00): '))
	hours_limit = int(input('How many hours per day will you gamble? '))
	days_limit = int(input('How many days do you have to gamble? '))
	print('\nHow fast would you like to run the simulation? Fast [f], Normal [n], or Slow [s]?')
	speed = input('(Slower is more accurate): ').lower()
	bet_loop = True
	
#Simulation loop
	while bet_loop == True:
		os.system('cls' if os.name == 'nt' else 'clear')
		print('\nRunning the simulations...')

		#Set base values
		session_count = int(0)	
		spin_count = int(0)
		days = int(0)
		hours = int(0)
		cash = starting_cash
		session_list = []
		perm_spins = []
		perm_spinstp = []
		perm_ending = []
		perm_ending_l = []
		perm_profit = []
		perm_hours = []
		perm_days = []

		#Simulate loop for X sessions.
		if speed == 'fast' or speed == 'f':
			sessions = int(21) 
		elif speed == 'normal' or speed == 'n':
			sessions = int(3000)
		elif speed == 'slow' or speed == 's':
			sessions = int(10000)

		#Progress bar settings
		pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=(sessions)).start()
		#Session loop
		for i in range(sessions):

			#Progress bar
			time.sleep(0.0001)
			pbar.update(i+1)
			
			#Bet until broke or time's up
			while cash > 0 and (spin_count * .03) < (hours_limit * days_limit) and bet <= cash:

				#Spin	
				current_spin = random.randint(1,38)
				spin_count += 1

				#Win/lose formulas
				if current_spin == number:
					cash = cash + (bet * 36)
				else:
					cash = cash - bet

# 				#Spins until profit
# 				spins_tp = [0]
# 				if cash <= starting_cash and (spin_count - 1) == spins_tp[-1]:
# 					spins_tp.append(spin_count)

				#Log in array
				session_list.append(cash)
			
				# Calculate time 
				if round(spin_count * .03) <1:
					hours = 1
				else:
					hours = round(spin_count * .03)
				days = math.ceil(hours / hours_limit)

			#Tally gambling session
			session_count = session_count + 1
			
			#Ending cash
			ending_cash = session_list[-1]
			perm_ending.append(ending_cash)
			
			#Find max profit
			session_list.sort()
			if (session_list[-1] - starting_cash) > 0:
				peak_profit = (session_list[-1] - starting_cash)
			else: 
				peak_profit = 0
			
			#Log loss for sessions with no profit
			if ending_cash < starting_cash and peak_profit == 0:
				perm_ending_l.append(ending_cash)

			#Permanent lists
			perm_spins.append(spin_count)
			perm_profit.append(peak_profit)
			perm_hours.append(hours)
			perm_days.append(days)
# 			perm_spinstp.append(spins_tp[-1])

			##Uncomment this to print results to a csv
			# import csv
			# with open('log.csv', 'a') as f:
			# 	w = csv.writer(f, quoting=csv.QUOTE_ALL)
			# 	w.writerow([peak_profit]) #change or add variables here

			#Reset stats on session
			session_list = []
			session_count = int(0)	
			spin_count = int(0)
			cash = starting_cash

		#Progress bar end
		pbar.finish()

	#Simulation output
		os.system('cls' if os.name == 'nt' else 'clear')
		print('\nSimulations complete. Compiling data...')
		
		#Remove outliers
		perm_hours.sort()
		if speed == 'fast' or speed == 'f':
			while len(perm_hours) > (sessions * .98):
				del perm_hours[-1]
		elif speed == 'normal' or speed == 'n':
			while len(perm_hours) > (sessions * .99):
				del perm_hours[-1]
		elif speed == 'slow' or speed == 's':
			while len(perm_hours) > (sessions * .995):
				del perm_hours[-1]
		perm_ending.sort()
		if speed == 'fast' or speed == 'f':
			while len(perm_ending) > (sessions * .98):
				del perm_ending[-1]
		elif speed == 'normal' or speed == 'n':
			while len(perm_ending) > (sessions * .99):
				del perm_ending[-1]
		elif speed == 'slow' or speed == 's':
			while len(perm_ending) > (sessions * .995):
				del perm_ending[-1]
		perm_profit.sort()
		if speed == 'fast' or speed == 'f':
			while len(perm_profit) > (sessions * .98):
				del perm_profit[-1]
		elif speed == 'normal' or speed == 'n':
			while len(perm_profit) > (sessions * .99):
				del perm_profit[-1]
		elif speed == 'slow' or speed == 's':
			while len(perm_profit) > (sessions * .995):
				del perm_profit[-1]
		
		#Calculate standard deviation
		n = len(perm_profit)
		mean = sum(perm_profit) / n
		mean_r = round(mean)
		var = sum((x - mean)**2 for x in perm_profit) / (n - 1)
		std_dev = round(var ** 0.5)

		#Calculate and format dev amounts
		dev1 = mean_r - std_dev * 2
		dev2 = mean_r - std_dev * 1
		dev3 = mean_r - std_dev * 0
		dev4 = mean_r - std_dev * -1
		dev5 = mean_r - std_dev * -2
		dev1_f = '{:,}'.format(dev1)
		dev2_f = '{:,}'.format(dev2)
		dev3_f = '{:,}'.format(dev3)
		dev4_f = '{:,}'.format(dev4)
		dev5_f = '{:,}'.format(dev5)
		
		#Calculate statistical analysis
		perm_ending_l.sort()
		starting_cash_f = '{:,}'.format(starting_cash)
		bet_f = '{:,}'.format(bet)
		sessions_f = '{:,}'.format(sessions)
		hours_limit_f = '{:,}'.format(hours_limit)
		days_limit_f = '{:,}'.format(days_limit)
		chance_loss = round((perm_profit.count(0) / len(perm_profit)) * 100, 1)
		chance_bust = round((perm_ending.count(0) / len(perm_profit)) * 100, 1)
		peak_profit_overall = '{:,}'.format(max(perm_profit))
		median_peak_profit = perm_profit[round((len(perm_profit) / 2) - 1)]
		median_peak_profit_f = '{:,}'.format(median_peak_profit)
		max_hours = max(perm_hours)
		max_days = max(perm_days)
		median_ending = perm_ending[round((len(perm_ending) / 2) - 1)]
		median_ending_l = perm_ending_l[round((len(perm_ending_l) / 2) - 1)]
		median_loss = median_ending_l - starting_cash
		median_hours = perm_hours[round((len(perm_hours) / 2) - 1)]
		profit_hour = round(median_peak_profit / median_hours)
		profit_hour_f = '{:,}'.format(profit_hour)
		median_hours_f = '{:,}'.format(median_hours)
		median_days_f = '{:,}'.format(perm_days[round((len(perm_days) / 2) - 1)])
		median_loss_f = '{:,}'.format(median_loss * -1)
		median_ending_f = '{:,}'.format(median_ending)

		#Print statistical analysis
		os.system('cls' if os.name == 'nt' else 'clear')
		print('Starting Cash: $' + starting_cash_f)
		print('Bet: $' + bet_f)
		print('Limit at table is ' + days_limit_f + ' days (at ' + hours_limit_f + ' hours per day)')
		print('\nThe following data is compiled from ' + sessions_f + ' simulations.') 
		print('Each simulation was played until the time limit was reached or the player could not cover their bet.')
		p1 = f'Median time at table: {median_hours_f} hours (over {median_days_f} days)'
		print('\n' + p1)
		p2 = f'Max time at table: {max_hours} hours (over {max_days} days)'
		print(p2)
		p3 = f'Median peak profit*: ${median_peak_profit_f} (${profit_hour_f}/hour)'
		print(p3)
		p4 = f'Max peak profit*: ${peak_profit_overall}'
		print(p4)
		p5 = f'Player has a {round(98 * ((100 - chance_loss) / 100),1)}% chance of peaking at: >${dev1_f} profit'
		if dev1 > 0:
			print('\n' + p5)
		p6 = f'Player has a {round(84 * ((100 - chance_loss) / 100),1)}% chance of peaking at: >${dev2_f} profit'
		if dev2 > 0:
			print(p6)
		p7 = f'Player has a {round(50 * ((100 - chance_loss) / 100),1)}% chance of peaking at: >${dev3_f} profit'
		if dev3 > 0:
			print(p7)
		p8 = f'Player has a {round(16 * ((100 - chance_loss) / 100),1)}% chance of peaking at: >${dev4_f} profit'
		if dev4 > 0:
			print(p8)
		p9 = f'Player has a {round(2 * ((100 - chance_loss) / 100),1)}% chance of peaking at: >${dev5_f} profit'
		if dev5 > 0:
			print(p9)
		p10 = f'Player has a {chance_loss}% chance of never making a profit (${median_loss_f} median loss)'
		print(p10)
		p11 = f'Player has a {chance_bust}% chance of going bust if they bet until time limit (${median_ending_f} median cash at time limit)'
		print(p11)
		print('\n*Peak profit is the highest cash value reached in a session') 
		print('after subtracting the player\'s starting cash.')
# 		print(perm_spinstp)
#		print(perm_profit)
#		print(perm_ending)
#		print(perm_ending_l)

	#End of simulation
		end_prompt = True
		while end_prompt == True:
			print('\nEnter \"c\" to calculate your chance at profiting a certain amount, \"b\" to change your bet, \"r\" to restart, or \"x\" to quit.')
			end_game = input().lower()
			
			#Options
			if end_game == 'c':
				query = int(input('\nEnter a dollar value: $').replace(',', ''))
				query_f = '{:,}'.format(query)
				z_score = (query - mean) / std_dev
				peak_chance = round((100 - st.norm.cdf(z_score) * 100) * ((100 - chance_loss) / 100), 1)
				eg1 = f'You have a {peak_chance}% chance of reaching a peak profit of ${query_f}'
				print('\n' + eg1)
			elif end_game == 'b':
				bet = int(input("\nHow much will you be betting per round?: $").replace(',', ''))
				end_prompt = False
			elif end_game == 'r':
				end_prompt = False
				bet_loop = False
			elif end_game == 'x':
				print('\nThanks for using Roulette Simulator!\n')
				sys.exit()
			else:
				print('\nInvalid input')








