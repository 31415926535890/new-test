@namespace
class SpriteKind:
    coin = SpriteKind.create()

def on_overlap_tile(sprite, undefined):
    pass
scene.on_overlap_tile(SpriteKind.player, None, on_overlap_tile)
