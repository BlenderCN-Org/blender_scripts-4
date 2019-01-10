
import sys
import bpy


def main(export_path):
  # switch to the export_scene
  bpy.context.screen.scene = bpy.data.scenes['export_scene']

  # switch to edit mode
  bpy.ops.object.mode_set(mode='EDIT')

  file_name = bpy.data.filepath.split("/")[-1].split(".")[0]
  file_path = "{ep}/uv_layout_{n}.png".format(ep=export_path, n=file_name)
  bpy.ops.uv.export_layout(filepath=file_path, size=(64, 64))


if __name__ == '__main__':
  main(sys.argv[-1])
