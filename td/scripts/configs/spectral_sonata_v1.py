# nosec
import sld_resolume_commands as resolume_commands
import random

transition_time = 0.9
frame_delay = 60
disable_third_layer = False

def isKeyBlack(key):
  offset = key % 12
  return offset in [2, 5, 7, 10, 0]

def choose_random_pattern():
  print("Choosing random pattern...")
  # for layer 1, just choose a random clip from 1-88
  clip_num = random.randint(1, 88)
  resolume_commands.activate_clip(1, clip_num)

  l2_num = random.randint(1, 88)
  if isKeyBlack(l2_num):
    run("clear_layer(2)", delayFrames=1*frame_delay, fromOP=op('sld_resolume_commands'))
    run("clear_layer(3)", delayFrames=2*frame_delay, fromOP=op('sld_resolume_commands'))
    run("activate_clip(4, {})".format(l2_num), delayFrames=3*frame_delay, fromOP=op('sld_resolume_commands'))
  else:
    run("activate_clip(2, {})".format(l2_num), delayFrames=1*frame_delay, fromOP=op('sld_resolume_commands'))
    run("activate_clip(3, {})".format(l2_num), delayFrames=2*frame_delay, fromOP=op('sld_resolume_commands'))
    run("clear_layer(4)", delayFrames=3*frame_delay, fromOP=op('sld_resolume_commands'))

  if disable_third_layer:
    return
  l3_num = random.randint(1, 88)
  if isKeyBlack(l3_num):
    run("clear_layer(5)", delayFrames=4*frame_delay, fromOP=op('sld_resolume_commands'))
    run("clear_layer(6)", delayFrames=5*frame_delay, fromOP=op('sld_resolume_commands'))
    run("activate_clip(7, {})".format(l3_num), delayFrames=6*frame_delay, fromOP=op('sld_resolume_commands'))
  else:
    run("activate_clip(5, {})".format(l3_num), delayFrames=4*frame_delay, fromOP=op('sld_resolume_commands'))
    run("activate_clip(6, {})".format(l3_num), delayFrames=5*frame_delay, fromOP=op('sld_resolume_commands'))
    run("clear_layer(7)", delayFrames=6*frame_delay, fromOP=op('sld_resolume_commands'))


def clear_patterns():
  for layer in range(1, 8):
    resolume_commands.clear_layer(layer)

  pass

def set_transition_times(num):
  for layer in range(1, 8):
    resolume_commands.update_transition_time(layer, num)
  return

def start():
  set_transition_times(transition_time)
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
