# me - this DAT.
#
# dat - the changed DAT
# rows - a list of row indices
# cols - a list of column indices
# cells - the list of cells that have changed content
# prev - the list of previous string contents of the changed cells
#
# Make sure the corresponding toggle is enabled in the DAT Execute DAT.
#
# If rows or columns are deleted, sizeChange will be called instead of row/col/cellChange.

current_values = [0, 0, 0]

def onTableChange(dat):
	return


def onRowChange(dat, rows):
  return


def onColChange(dat, cols):
	return


def onCellChange(dat, cells, prev):
   onSizeChange(dat)
   return


# white keys: 1 - 52
# black keys: 53 - 86
def getPianoMap():
  black_keys = []
  white_keys = []
  for i in range(1, 89):
    offset = i % 12
    if offset in [2, 5, 7, 10, 0]:
      black_keys.append(i)
    else:
      white_keys.append(i)
  piano_map = [0] + white_keys + black_keys
  # invert the piano_map so that the keys are the values and the values are the keys
  piano_map = {v: k for k, v in enumerate(piano_map)}

  return piano_map

piano_map = getPianoMap()

def updateResolume(row, value):
  print(f"Updating Resolume for row {row} with value {value}")
  resolume = mod('/project1/ui_container/resolume_container/sld_resolume_commands')

  if row in [1]:
    if value == 0:
      resolume.clear_layer(1)
    else:
      resolume.activate_clip(1, value)
  elif row in [2]:
    print("would map value to piano key:", value, piano_map[value])
    if value == 0:
      resolume.clear_layer(2)
      resolume.clear_layer(3)
      resolume.clear_layer(4)
    else:
      val = piano_map[value]
      if val < 53:
        resolume.activate_clip(2, val)
        resolume.activate_clip(3, val)
        resolume.clear_layer(4)
      else:
        resolume.clear_layer(2)
        resolume.clear_layer(3)
        resolume.activate_clip(4, val)
  elif row in [3]:
    if value == 0:
      resolume.clear_layer(5)
      resolume.clear_layer(6)
      resolume.clear_layer(7)
    else:
      val = piano_map[value]
      if val < 53:
        resolume.activate_clip(5, val)
        resolume.activate_clip(6, val)
        resolume.clear_layer(7)
      else:
        resolume.clear_layer(5)
        resolume.clear_layer(6)
        resolume.activate_clip(7, val)
  return

def onSizeChange(dat):
  # print(f"Table size changed to {dat.numRows} rows and {dat.numCols} columns")
  # print(dat[1, 0].val)
  for i in range(1, 4):
    try:
      if dat[i, 0] is None:
        if current_values[i-1] != 0:
          current_values[i-1] = 0
          print(f"Value in row {i} changed to 0")
          updateResolume(i, 0)
      else:
        new_value = int(dat[i, 0].val)
        if new_value != current_values[i-1]:
          # its changed so call resolume
          current_values[i-1] = new_value
          print(f"Value in row {i} changed to {new_value}")
          updateResolume(i, new_value)
    except ValueError:
      print("got a value error so setting to 0")
      current_values[i-1] = 0
  print(f"Current values: {current_values}")
  return
