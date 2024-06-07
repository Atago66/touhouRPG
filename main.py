#unfinished, finishing the story
import os
import sys
import random
import time
import json



player_stats=[0,0,0,0]
def save_player_stats(player_stats, file_path='savegame.json'):
	with open(file_path, 'w') as file:
					json.dump(player_stats, file)

def load_player_stats(file_path='savegame.json'):
	global player_stats
	try:
					with open(file_path, 'r') as file:
									player_stats = json.load(file)
					return player_stats
	except FileNotFoundError:
					# Handle the case where the file doesn't exist yet
					return player_stats

character='placeholder'
character_level_total=0
character_health_level=0
character_attack_level=0
character_defense_level=0


load_player_stats(file_path='savegame.json')



def clear():
	if os.name==('nt'):
		os.system('cls')
	else:
		os.system('clear')
textdelay = lambda: time.sleep(3)
endterminal = lambda: os.system('exit')

finished_game=False



class Player:
				def __init__(self, name, health, attack, defense):
								self.name = name
								self.max_health = health
								self.health = health
								self.attack = attack
								self.defense = defense
								self.inventory = {'Potion': 3, 'Spell Card': 1,}

#damage, healing, and life checks (player)
				def take_damage(self, damage):
								if damage<0:
												damage=1
								self.health -= damage
								if self.health < 0:
												self.health = 0

				def heal(self, amount):
								self.health += amount
								if self.health > self.max_health:
												self.health = self.max_health

				def is_alive(self):
								return self.health > 0


class Enemy:
				def __init__(self, name, health, attack, defense):
								self.name = name
								self.health = health
								self.attack = attack
								self.defense = defense

#enemy damagehealing and life check
				def take_damage(self, damage):
								if damage<0:
												damage=1
								self.health -= damage
								if self.health < 0:
												self.health = 0

				def is_alive(self):
								return self.health > 0


class Item:
				def __init__(self, name, description, healing_amount):
								self.name = name
								self.description = description
								self.healing_amount = healing_amount


#enemy lists
enemies = [
								Enemy('Star Sapphire', 10, 4, 0), 
								Enemy('Cirno', 20, 7, 1),
								Enemy('Nitori Kawashiro', 30, 11, 5),
								Enemy('Utsuho Reiuji', 40, 9, 4),
								Enemy('Youmu Konpaju', 30, 11, 5),
								Enemy('Yuyuko Saigyouji', 40, 9, 4),
								Enemy('Tewi Inaba', 50, 11, 5),
								Enemy('Reisen Undongein Inaba', 60, 13, 6),
								Enemy('Reisen Undongein Inaba', 70, 15, 6),
								Enemy('Nue Houjuu', 80, 16, 7),
								Enemy('Flandre Scarlet', 65, 23, 5),
								Enemy('Remilia Scarlet', 75, 19, 6),
								Enemy('Yukari Yakumo', 85, 25, 5),
								Enemy('Koishi Komeji', 60, 40, 1),
								Enemy('Doremi Sweet', 60, 22, 7),
								Enemy('Fujiwara no Mokou', 130, 30, 7),
								Enemy('Patchouli Knowledge', 70, 20, 7),
								Enemy('Seija Kijin', 80, 24, 8), 
								Enemy('Satori Komeji', 70, 30, 4),
								Enemy('Ran Yakumo', 75, 23, 6),
								Enemy('Sanae Kochiya', 75, 21, 6),
								Enemy('Youmu Konpaju (EX)', 60, 22, 6),
								Enemy('Yuyuko Saigyouji (EX)', 80, 25, 8),
								Enemy('Nitori Kawashiro (EX)', 60, 20, 6),
								Enemy('Utsuho Reiuji (EX)', 80, 24, 7),
								Enemy('Tewi Inaba (EX)', 100, 20, 5),
								Enemy('Reisen Undongein Inaba (EX)', 140, 26, 5),




				]
#characters (sakuya is my favorite :) )
def character_selection():
				global character
				print('Select your character:')
				print('1. Reimu Hakurei: Shrine Maiden')
				print('2. Marisa Kirisame: Human Magician')
				print('3. Sakuya Izayoi: Time-stopping Maid')
				print('4. Rumia: Simple-minded Darkness Controller')

				choice = input('Enter the number of your choice: ')

				if choice == '1':
								time.sleep(1)
								character='Reimu'
								return Player('Reimu Hakurei', 100, 11, 4), get_reimu_dialogues()
				elif choice == '2':
								time.sleep(1)
								character='Marisa'
								return Player('Marisa Kirisame', 80, 15, 4), get_marisa_dialogues()
				elif choice == '3':
								time.sleep(1)
								character='Sakuya'
								return Player('Sakuya Izayoi', 90, 17, 2), get_sakuya_dialogues()
				elif choice == '4':
								time.sleep(1)
								character='Rumia'
								return Player('Rumia', 75, 17, 6), get_rumia_dialogues()
				else:
								print('Invalid choice. Defaulting to Reimu Hakurei... Because who DOESN\'T like Reimu :)')
								character='Reimu'
								return Player('Reimu Hakurei', 100, 12, 5), get_reimu_dialogues()

#dialogues for each character during specific events
def get_reimu_dialogues():
				return {
								'start': 'Reimu: I am Reimu Hakurei, the Hakurei shrine maiden. '
																	'Reimu: Prepare to meet your end...',
								'defeated_enemy': 'Reimu: You\'re more of an annoyance than anything...',
								'victory': 'Reimu: Stop wasting my time...',
								'defeat': 'Reimu: Damn... you...',
								'use_item': 'Reimu: Marisa\'s Potion... she\'s the best...',
								'run_fail': 'Reimu: I can\'t escape...I must prepare for battle.',
								'use_card': 'Reimu: Your time has come... Fantasy Seal!'
				}

def get_marisa_dialogues():
				return {
								'start': 'Marisa: Hey there! I\'m Marisa Kirisame, the human magician with not-so-human abilities! '
																	'Marisa: Prepare yourself!',
								'defeated_enemy': 'Marisa: Another one bites the dust! ♩ I\'m on fire!',
								'victory': 'Marisa: Now, let\'s keep going.',
								'defeat': 'Marisa: I think... I\'ll get \'em next time...',
								'use_item': 'Marisa: My potions are pretty handy! They\'ll get you back on your feet in no time.',
								'run_fail': 'Marisa: No escape for me this time. Gonna stand my ground!',
								'use_card': 'Marisa: You ready?! Master Spark!!!'
				}

def get_sakuya_dialogues():
				return {
								'start': 'Sakyua: Greetings. I am Sakuya Izayoi, the maid of the Scarlet Devil Mansion. '
																	'Sakuya: Time manipulation is my specialty... although it would be a waste on something so weak.',
								'defeated_enemy': 'Sakuya: Another foe vanquished. Time itself bends to my will.',
								'victory': 'Sakuya: That was simple, really.',
								'defeat': 'Sakuya: It seems our time has run out...',
								'use_item': 'Sakuya: A potion... it\'s nothing fancy, but it should help in a pinch.',
								'run_fail': 'Sakuya: Retreating is not always an option. I must prepare to battle.',
								'use_card': 'Sakuya: Perish before my knife...'
				}

def get_rumia_dialogues():
				return {
									'start': 'Rumia: Hey... It\'s pretty cold right now...I like the cold... and the dark.',
								'defeated_enemy': 'Rumia: I\'m used to the dark... obviously you were gonna lose.',
								'victory': 'Rumia: An easy win...',
								'defeat': 'Rumia: Not... like... this...',
								'use_item': 'Rumia: A potion... it\'s kinda cold.',
								'run_fail': 'Rumia: Can\'t hide... I need to fight.',
								'use_card': 'Rumia: It\'s over for you...'
								}
def display_dialogue(dialogues, event):
				if event in dialogues:
								print(dialogues[event])

def get_item(item_name):
				items = {
								'Potion': Item('Potion', 'Heals for 20 health', 20),
								'Spell Card': Item('Spell Card', 'Deals 20 damage in a single hit.', 0)

				}
				return items.get(item_name, None)

def battle(player, enemy, character_dialogues):
				textdelay()
				print(f'{enemy.name} appears!')
				print()
				textdelay()

				display_dialogue(character_dialogues, 'start')

#when alive, display stats
				while player.is_alive() and enemy.is_alive():
								time.sleep(1)
								print(f'\n{character}\'s Stats:')
								print(f'Health: {player.health}/{player.max_health}')
								print(f'Attack: {player.attack}')
								print(f'Defense: {player.defense}')
								print(f'Inventory: {player.inventory}\n')

								time.sleep(1)
								print(f'{enemy.name} Stats:')
								print(f'Health: {enemy.health}')
								print(f'Attack: {enemy.attack}')
								print(f'Defense: {enemy.defense}\n')

#actions
								textdelay()
								action = input('What do you want to do? (1. Attack, 2. Use Item, 3. Run) ')

								if action == '1':
												textdelay()
												player_damage = random.randint(1, player.attack)
												enemy_damage = random.randint(1, enemy.attack)

												player.take_damage(enemy_damage - player.defense)
												enemy.take_damage(player_damage - enemy.defense)

												if player_damage - enemy.defense <= 0:
																print(f'You dealt 1 damage to {enemy.name}.')
																textdelay()
												else:
																print(f'You dealt {player_damage - enemy.defense} damage to {enemy.name}.')
																textdelay()

												if enemy_damage - player.defense <= 0:
																print (f'{enemy.name} dealt 1 damage to you.')
																textdelay()
												else:
																print(f'{enemy.name} dealt {enemy_damage - player.defense} damage to you.')

																textdelay()
												clear

								elif action == '2':
												textdelay()
												print('Inventory:')
												for item, quantity in player.inventory.items():
																print(f'{item}: {quantity}')
												item_choice = input('Choose an item to use: ')
												if item_choice in player.inventory and player.inventory[item_choice] > 0:
																item = get_item(item_choice)
																if item_choice == 'Potion':
																				player.heal(item.healing_amount)
																				textdelay()
																				print(f'You used {item.name} and healed for {item.healing_amount} health.')
																				textdelay()
																				display_dialogue(character_dialogues, 'use_item')
																				player.inventory[item_choice] -= 1
																elif item_choice == 'Spell Card':
																				enemy.take_damage(20)
																				textdelay()
																				display_dialogue(character_dialogues, 'use_card')
																				textdelay()
																				print(f'You used your spell card! Dealt 20 damage.')
																				player.inventory[item_choice] -= 1



								elif action == '3':
												time.sleep(1)
												if random.random() < 0.5:  # 50% chance of successfully running away
																print('You managed to escape.')
																return
												else:
																display_dialogue(character_dialogues, 'run_fail')
								else:
												textdelay()
												print ('Select a valid option.')

				if player.is_alive():
								global character_level_total, character_health_level, character_attack_level, character_defense_level
								textdelay()
								print(f'You defeated {enemy.name}!')
								textdelay()
								display_dialogue(character_dialogues, 'defeated_enemy')
								print ('\n'*2)
								textdelay()

								level_up_type=random.choice(["health","attack","defense","none"])						   	
								if level_up_type=="health":
									player.max_health=player.max_health+5
									print ('Health level up!')
									character_level_total=character_level_total+1
									character_health_level=character_health_level+1
									textdelay()
								if level_up_type=="attack":
									player.attack=player.attack+2
									print ('Defense level up!')
									character_level_total=character_level_total+1
									character_attack_level=character_attack_level+1
									textdelay()
								if level_up_type=="defense":
									player.defense=player.defense+1
									print ('Defense level up!')
									character_level_total=character_level_total+1
									character_defense_level=character_defense_level+1
									textdelay()
								if level_up_type=="none":
									print ('No level up... tough luck.')
									textdelay()

								player_stats = [
									character_level_total,
									character_attack_level,
									character_health_level,
									character_defense_level,

								]
								save_player_stats(player_stats, file_path='savegame.json')
								print (f'Character level is now {character_level_total}!')


								loot = random.choice(['Potion', 'Spell Card'])
								print(f'You found a {loot}.')
								if loot in player.inventory:
												player.inventory[loot] += 1
								else:
												player.inventory[loot] = 1
				else:
								print('Game over. You were defeated.')
								display_dialogue(character_dialogues, 'defeat')


def double_battle(player, enemy, enemy1, character_dialogues):
				textdelay()
				print(f'{enemy.name} and {enemy1.name} appear!')
				print()
				time.sleep (2)

				while player.is_alive() and enemy.is_alive and enemy1.is_alive():
								time.sleep(1)
								print(f'\n{character}\'s Stats:')
								print(f'Health: {player.health}/{player.max_health}')
								print(f'Attack: {player.attack}')
								print(f'Defense: {player.defense}')
								print(f'Inventory: {player.inventory}\n')

								time.sleep(1)
								print(f'{enemy.name} Stats:')
								print(f'Health: {enemy.health}')
								print(f'Attack: {enemy.attack}')
								print(f'Defense: {enemy.defense}\n')

								time.sleep(1)
								print(f'{enemy1.name} Stats:')
								print(f'Health: {enemy1.health}')
								print(f'Attack: {enemy1.attack}')
								print(f'Defense: {enemy1.defense}\n')

#actions
								textdelay()
								action = input('What do you want to do? (1. Attack, 2. Use Item, 3. Run) ')

								if action == '1':
												textdelay()
												player_damage = random.randint(1, player.attack)
												player_damage1 = random.randint(1, player.attack)
												enemy_damage = random.randint(1, enemy.attack)
												enemy1_damage = random.randint(1, enemy1.attack)

												player.take_damage(enemy_damage - player.defense)
												player.take_damage(enemy1_damage - player.defense)
												enemy.take_damage(player_damage - enemy.defense)
												enemy1.take_damage(player_damage1 - enemy1.defense)

												if player_damage - enemy.defense <= 0:
																print(f'You dealt 1 damage to {enemy.name}.')
																textdelay()
												else:
																print(f'You dealt {player_damage - enemy.defense} damage to {enemy.name}.')
																textdelay()

												if enemy_damage - player.defense <= 0:
																print (f'{enemy.name} dealt 1 damage to you.')
																textdelay()
												else:
																print(f'{enemy.name} dealt {enemy_damage - player.defense} damage to you.')
																textdelay()

												if player_damage1 - enemy1.defense <= 0:
																print(f'You dealt 1 damage to {enemy1.name}.')
																textdelay()
												else:
																print(f'You dealt {player_damage1 - enemy1.defense} damage to {enemy1.name}.')
																textdelay()

												if enemy1_damage - player.defense <= 0:
																print (f'{enemy1.name} dealt 1 damage to you.')
																textdelay()
												else:
																print(f'{enemy1.name} dealt {enemy1_damage - player.defense} damage to you.')
																textdelay()
												clear

								elif action == '2':
												textdelay()
												print('Inventory:')
												for item, quantity in player.inventory.items():
																print(f'{item}: {quantity}')

												item_choice = input('Choose an item to use: ')
												if item_choice in player.inventory and player.inventory[item_choice] > 0:
																item = get_item(item_choice)
																if item_choice == 'Potion':
																				player.heal(item.healing_amount)
																				textdelay()
																				print(f'You used {item.name} and healed for {item.healing_amount} health.')
																				textdelay()
																				display_dialogue(character_dialogues, 'use_item')
																				player.inventory[item_choice] -= 1
																elif item_choice == 'Spell Card':
																				enemy.take_damage (15)
																				enemy1.take_damage (15)
																				textdelay()
																				display_dialogue(character_dialogues, 'use_card')
																				textdelay()
																				print(f'You used your spell card! Dealt 20 damage.')
																				player.inventory[item_choice] -= 1



												else:
																print('Invalid item choice. Try again.')

								elif action == '3':
												time.sleep(1)
												if random.random() < 0.5:  # 50% chance of successfully running away
																print('You managed to escape.')
																return
												else:
																display_dialogue(character_dialogues, 'run_fail')
								else:
												textdelay()
												print ('Select a valid option.')

				if player.is_alive():
								level_up_type=random.choice(["health","attack","defense","none"])						   	
								if level_up_type=="health":
									player.max_health=player.max_health+5
									print ('Health level up!')
									character_level_total=character_level_total+1
									character_health_level=character_health_level+1
									textdelay()
								if level_up_type=="attack":
									player.attack=player.attack+2
									print ('Defense level up!')
									character_level_total=character_level_total+1
									character_attack_level=character_attack_level+1
									textdelay()
								if level_up_type=="defense":
									player.defense=player.defense+1
									print ('Defense level up!')
									character_level_total=character_level_total+1
									character_defense_level=character_defense_level+1
									textdelay()
								if level_up_type=="none":
									print ('No level up... tough luck.')
									textdelay()

								player_stats = [
									character_level_total,
									character_attack_level,
									character_health_level,
									character_defense_level,

								]
								save_player_stats(player_stats, file_path='savegame.json')
								print (f'Character level is now {character_level_total}!')



								loot = random.choice(['Potion', 'Potion', 'Potion', 'Spell Card'])
								print(f'You found a {loot}.')
								print('\n'*2)
								if loot in player.inventory:
												player.inventory[loot] += 1
								else:
												player.inventory[loot] = 1
				else:
								print('Game over. You were defeated.')
								display_dialogue(character_dialogues, 'defeat')


def show_title_screen():
				print('*******************************')
				print('* TOUHOU: TAIYŌ NO NAI SORA!  *')
				print('*******************************')
				print('*        1. Start Game        *')
				print('*        2. Information       *')
				print('*        3. Extra Mode        *')
				print('*        4. Reset Game        *')
				print('*        5. Quit              *')
				print('*******************************')
				print()
#this is where the events of the game actually start, story and combat sequences are staged here
def start_game():
				global finished_game, character_level_total, character_health_level, character_attack_level, character_defense_level, player_stats
				while True:
								show_title_screen()
								choice = input('Enter the number of your choice: ')
								if choice == '1':
												textdelay()
												player, character_dialogues = character_selection()
												for i in range (player_stats[2]):
													player.max_health=player.max_health+5
												for i in range (player_stats[1]):
													player.attack=player.attack+2
												for i in range (player_stats[3]):
													player.defense=player.defense+1
												print ('\n'*2)
												textdelay()
												clear()
												print ('Gensokyo, Japan')
												textdelay()
												print ('The time is 8:00am, yet it is still pitch black oustide...')
												textdelay()
												print ('A heavy and dense fog has descended everywhere, and the air is cold...')
												textdelay()
												print ('*')
												textdelay()
												print ('*')
												textdelay()
												print ('*')
												textdelay()
												print ('THUD!')
												textdelay()
												print (f'*{character} wakes up on the floor.*')
												textdelay()
												print (f'{character}: What the...?')
												textdelay()
												print (f'{character}: Why is it so dark?')
												textdelay()
												print ('BONK!')
												textdelay()
												print (f'{character}: OW! My head... what the hell is happening...?')
												textdelay()
												print (f'*{character} stumbles around her room, trying to find her clothes and get ready for the day.*')
												textdelay()
												if character=="Reimu":
																print(f'{character}: I suppose it\'s my job to handle this... isn\'t it?')
												elif character=="Marisa":
																print (f'{character}: I\'m gonna handle this for Reimu! She\'ll be so proud of me!')
												elif character=='Sakuya':
																print (f'{character}: I suppose it\'s my duty to handle this.')
												elif character=='Rumia':
																print (f'{character}: I should do something about this probably...')
												textdelay()
												print (f'{character}: But how..?')
												textdelay()
												print (f'*{character} slowly makes her way towards the Forest near the Hakurei Shrine,\n blindly bumping into many things on the way there.*')
												textdelay()
												print ('Upon getting to the lake, a screaming voice can be heard...')
												textdelay()
												print ('Star Sapphire: WHO GOES THERE!')
												textdelay()
												print (f'{character}: I\'m not here for a fight, I need your help.')
												textdelay()
												print ('Star Sapphire: Why should I help you?!')
												textdelay()
												print ('Star Sapphire: With my power, I\'m perfectly capable of sensing moving objects!')
												textdelay()
												print ('Star Sapphire: I can see better than anyone else right now!')
												textdelay()
												print ('Star Sapphire: And, I\'m sure that can fix this myself!')
												textdelay()
												if character=="Reimu":
																print(f'{character}: Sure you can...')
												elif character=="Marisa":
																print (f'{character}: Yeah, okay... that\'s a funny joke!')
												elif character=='Sakuya':
																print (f'{character}: You should rethink that sentiment...')
												elif character=='Rumia':
																print (f'{character}: Whatever you say...')
												textdelay()
												print ('Star Sapphire: You think I can\'t?! Watch this!')
												print()
												textdelay()
												clear()

												current_enemy = enemies[0]
												battle(player, current_enemy, character_dialogues)

												clear()
												print ('Star Sapphire: STOP! STOP! I\'ll help you!')
												textdelay()
												print ('A faint high-pitched voice can be heard approaching.')
												textdelay()
												print ('Cirno: Don\'t back down! I can win this!')
												textdelay()
												print ('Star Sapphire: Wait! I-')
												time.sleep(1)
												print ('Cirno: Prepare to fight!')
												time.sleep (2)
												print ('Cirno: I, the strongest fairy, will defeat you!')
												textdelay()
												if character=="Reimu":
																print(f'{character}: Not this again...')
												elif character=="Marisa":
																print (f'{character}: Do I really have to kick some fairy ass again?!')
												elif character=='Sakuya':
																print (f'{character}: Yet another small fairy-shaped roadblock...')
												elif character=='Rumia':
																print (f'{character}: Oh... another one to fight...')
												textdelay()
												clear()

												current_enemy = enemies[1]
												battle(player, current_enemy, character_dialogues)

												clear()
												print ('Cirno: AHHH! I\'m sorry! I- I\'ll stop!')
												textdelay()
												if character=="Reimu":
																print(f'{character}: Yeah, you WILL stop...')
												elif character=="Marisa":
																print (f'{character}: Didn\'t even break a sweat Cirno!')
												elif character=='Sakuya':
																print (f'{character}: Good... now we can get to business.')
												elif character=='Rumia':
																print (f'{character}: Okay... help me fix this...')
												textdelay()
												if character=="Reimu":
																print(f'{character}: I need your power... so I can "see."')
												elif character=="Marisa":
																print (f'{character}: You\'re gonna let me use your power!')
												elif character=='Sakuya':
																print (f'{character}: I\'ll be borrowing your power for a bit.')
												elif character=='Rumia':
																print (f'{character}: Your power... maybe it can help?')
												textdelay()
												print('Star Sapphire: I guess that\'s fine... if it stops all of this.')
												textdelay()
												print('Star Sapphire: But where do we even go first?')
												time.sleep (2)
												if character == 'Reimu' or character == 'Marisa' or character == 'Sakuya':
																print(f'{character}: I think I have an idea of who may be doing this...')
												elif character=='Rumia':
																print ('Rumia: Maybe I have an idea of where to go..?')
												textdelay()
												clear()
												print('-----END OF PART 1-----')

												textdelay()
												clear()

												print('**********************************')
												print('*             Paths:             *')
												print('**********************************')
												print('*  1. Underground Geyser Center  *')
												print('*                                *')
												print('*  2. The Netherworld            *')
												print('**********************************')
												print()

												textdelay()
												path1 = input ('Where will you go next? (Enter number of choice:)')
												if path1=='1':
															clear()
															textdelay()
															print(f'*{character} and Star make their way to the Underground Geyser Center.*')
															textdelay()
															print ('They bump into fewer things with Star\'s power...')
															textdelay()
															print ('...but still come out bruised.')
															textdelay()
															print ('An intense heat and light are emitted from the Geyser Center.')
															textdelay()
															print ('It can be seen glowing through the fog brightly.')
															textdelay()
															print('Star Sapphire: Wait... Someone\'s here...')
															textdelay()
															print('*She stops, focusing.*')
															textdelay()
															print('Star Sapphire: It\'s a Kappa!')
															textdelay()
															print('Star Sapphire: We\'re kinda trespassing on their property aren\'t we..?')
															textdelay()
															if character=='Sakuya':
																		print(f'{character}: I suppose we are...')
															else:
																		print(f'{character}: Yeah...')
															textdelay()
															print (f'*{character} and Star Sapphire approach, hearing a fanit voice...*')
															textdelay()
															print ('Nitori Kawashiro: Leave us alone!')
															textdelay()
															print ('Star Sapphire: She\'s running away!')
															textdelay()
															print ('Star Sapphire: She has to be responsible for this!')
															textdelay()
															if character=="Reimu":
																print(f'{character}:Don\'t worry... she isn\'t getting away.')
															elif character=="Marisa":
																print (f'{character}:Get her!!!')
															elif character=='Sakuya':
																print (f'{character}: So unnecessary...')
															elif character=='Rumia':
																print (f'{character}: Should we chase her?')
															textdelay()
															print (f'*{character} and Star run close behind Nitori, getting very close to her*')
															textdelay()
															print ('*Nitori is cornered by tree branches...*')
															textdelay()
															print ('Star Sapphire: It\'s over for you now!')
															textdelay()
															current_enemy = enemies[2]
															battle(player, current_enemy, character_dialogues)
															print ('Nitori Kawashiro: We didn\'t do this..! Get away!')
															textdelay()
															print ('Star Sapphire: Then who else could\'ve done this?')
															textdelay()
															print ('Star Sapphire: It must\'ve been you!')
															textdelay()
															print ('Nitori Kawashiro: I really need to get bck to the geyser center...')
															textdelay()
															print ('Nitori Kawashiro: It\'s important... I promise I didn\'t have any part in this.')
															textdelay()
															print ('*A deep rumbling can be heard.*')
															textdelay()
															print ('Nitori Kawashiro: Oh no...')
															textdelay()
															print ('Nitori Kawashiro: This is the last time I\'ll try to charge a battery witth nuclear energy...')
															textdelay()
															print ('*A bright orange glow can be seen in the fog getting larger*')
															textdelay()
															print ('Nitori Kawashiro: DUCK!')
															textdelay()
															current_enemy = enemies[3]
															battle(player, current_enemy, character_dialogues)
															print ('Utsuho Reiuji: ')




												elif path1=='2':
															print()







												finished_game=True












								elif choice == '2':
												print('Touhou: Taiyō No Nai Sora is a fanwork of ZUN\'s Touhou Project,\n it is a simple text-based RPG made for a Computer Science Intro Class...')
												textdelay()
												print('...although 99% of it was made out of class.')
												textdelay()
												print('The game\'s text-based nature is justified by the thick and dark mist present in the game...')
												textdelay()
												print('...creative, right? :)')
												textdelay()
												print('I\'m not very good at Python, so excuse the unoptimized code.')
												time.sleep(5)
												print ('\n' * 3 )
												clear()

								elif choice == '3':
												if finished_game==False:
																print('Extra Mode is locked until game has been completed.')
																textdelay()
																clear()
												elif finished_game==True:
																print ('Extra Mode contains battles with a random assortment of character that weren\'t included in the main game.')
																textdelay()
																print('...They are not canonical fights...')
																print()
																textdelay()
																print ('Select a character to challenge Extra Mode with:')
																print()
																textdelay()
																player, character_dialogues = character_selection()
																textdelay()


																print()
																print('**********************************')
																print('*          Extra Bosses:         *')
																print('**********************************')
																print('*       1. Nue Houjuu            *')
																print('*       2. Flandre Scarlet       *')
																print('*       3. Remilia Scarlet       *')
																print('*       4. Yukari Yakumo         *')
																print('*       5. Koishi Komeji         *')
																print('*       6. Doremi Sweet          *')
																print('*       7. Fujiwara no Mokou     *')
																print('*       8. Patchouli Knowledge   *')
																print('*       9. Seija Kijin           *')
																print('*       10. Double Battles (Pg.2)*')
																print('**********************************')
																print()

																extra_fight=int(input('Choose an Extra Boss:'))
																if extra_fight==1:
																	current_enemy = enemies[9]
																	battle(player, current_enemy, character_dialogues)
																elif extra_fight==2:
																	current_enemy = enemies[10]
																	battle(player, current_enemy, character_dialogues)
																elif extra_fight==3:
																	current_enemy = enemies[11]
																	battle(player, current_enemy, character_dialogues)
																elif extra_fight==4:
																	current_enemy = enemies[12]
																	battle(player, current_enemy, character_dialogues)
																elif extra_fight==5:
																	current_enemy = enemies[13]
																	battle(player, current_enemy, character_dialogues)
																elif extra_fight==6:
																	current_enemy = enemies[14]
																	battle(player, current_enemy, character_dialogues)
																elif extra_fight==7:
																	current_enemy = enemies[15]
																	battle(player, current_enemy, character_dialogues)
																elif extra_fight==8:
																	current_enemy = enemies[16]
																	battle(player, current_enemy, character_dialogues)
																elif extra_fight==9:
																	current_enemy = enemies[17]
																	battle(player, current_enemy, character_dialogues)
																elif extra_fight==10:

																	print()
																	print('**********************************')
																	print('*          Extra Bosses:*         ')
																	print('*         (Double Battles)        ')
																	print('**********************************')
																	print('*       1. Remilia and Flandre   *')
																	print('*       2. Koishi and Satori     *')
																	print('*       3. Yukari and Ran        *')
																	print('*       4. Youmu and Yuyuko (EX) *')
																	print('*       5. Nitori and Utsuho (EX)*')
																	print('*       6. Tewi and Reisen (EX)  *')
																	print('*                                *')
																	print('*                                *')
																	print('*                                *')
																	print('*       7. Back                  *')
																	print('**********************************')
																	print()

																	double_battle_extra=int(input('Enter an Extra Double Battle:'))
																	if double_battle_extra==1:
																		current_enemy=enemies[10]
																		current_enemy1=enemies[11]
																		double_battle(player, current_enemy, current_enemy1, character_dialogues)
																	elif double_battle_extra==2:
																		current_enemy=enemies[13]
																		current_enemy1=enemies[18]
																		double_battle(player, current_enemy, current_enemy1, character_dialogues)
																	elif double_battle_extra==3:
																		current_enemy=enemies[12]
																		current_enemy1=enemies[19]
																		double_battle(player, current_enemy, current_enemy1, character_dialogues)
																	elif double_battle_extra==4:
																		current_enemy=enemies[21]
																		current_enemy1=enemies[22]
																		double_battle(player, current_enemy, current_enemy1, character_dialogues)
																	elif double_battle_extra==5:
																		current_enemy=enemies[23]
																		current_enemy1=enemies[24]
																		double_battle(player, current_enemy, current_enemy1, character_dialogues)
																	elif double_battle_extra==6:
																		current_enemy=enemies[25]
																		current_enemy1=enemies[26]
																		double_battle(player, current_enemy, current_enemy1, character_dialogues)
																	elif double_battle_extra==7:
																		show_title_screen







								elif choice == '4':
									player_stats=[0,0,0,0]
									save_player_stats(player_stats)
									break
								elif choice == '5':
												print('Goodbye!')
												textdelay()
												clear()
												endterminal
												break
								else:
												print('Invalid choice.')


if __name__ == '__main__':
				start_game()