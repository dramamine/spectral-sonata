# nosec
import sld_resolume_commands as resolume_commands
import random

def isKeyBlack(key):
  offset = key % 12
  return offset in [2, 5, 7, 10, 0]

def choose_random_pattern():
  print("Choosing random pattern...")
  # for layer 1, just choose a random clip from 1-88
  # use the random library to get an integer between 1 and 88 inclusive
  clip_num = random.randint(1, 88)
  resolume_commands.activate_clip(1, clip_num)

  # for layer 2:
  l2_num = random.randint(1, 88)
  if isKeyBlack(l2_num):
    resolume_commands.clear_layer(2)
    resolume_commands.clear_layer(3)
    resolume_commands.activate_clip(4, l2_num)
  else:
    resolume_commands.activate_clip(2, l2_num)
    resolume_commands.activate_clip(3, l2_num)
    resolume_commands.clear_layer(4)

  l3_num = random.randint(1, 88)
  if isKeyBlack(l3_num):
    resolume_commands.clear_layer(5)
    resolume_commands.clear_layer(6)
    resolume_commands.activate_clip(7, l2_num)
  else:
    resolume_commands.activate_clip(5, l2_num)
    resolume_commands.activate_clip(6, l2_num)
    resolume_commands.clear_layer(7)

  pass

def clear_patterns():
  for layer in range(1, 9):
    resolume_commands.clear_layer(layer)

  pass

def set_transition_times(num):
  for layer in range(1, 8):
    resolume_commands.update_transition_time(layer, num)
  return

def start():
  set_transition_times(4)
  resolume_commands.activate_clip(8, 1)
  choose_random_pattern()
  return

def stop():
  set_transition_times(0)
  resolume_commands.activate_clip(8, 2)
  clear_patterns()
  return

# def get_intensity():
#   return int(op('intensity_chop')[0, 0])

# def set_intensity(num):
#   global intensity
#   intensity = num
#   return


# def choose_intensity(num):
#   set_intensity(num)
#   op('/project1/ui_container/resolume_container/knobFixed').par.Value0 = num/19
#   ast.load(random.choice(intensity_templates[num]))
#   ast.prepare()
#   return
