@namespace
class SpriteKind:
    thing = SpriteKind.create()
    thing2 = SpriteKind.create()
    thing3 = SpriteKind.create()
    thing4 = SpriteKind.create()
def level4():
    global NumRandom, level, mySprite
    NumRandom = randint(1, 4)
    level += 1
    sprites.destroy_all_sprites_of_kind(SpriteKind.thing3)
    Render.get_render_sprite_instance().set_kind(SpriteKind.player)
    mySprite = sprites.create(assets.image("""
        thing
        """), SpriteKind.thing4)
    tiles.place_on_tile(mySprite, tiles.get_tile_location(14, 14))
    scene.set_background_image(assets.image("""
        background
        """))
    tiles.place_on_tile(Render.get_render_sprite_instance(),
        tiles.get_tile_location(1, 1))
    if NumRandom == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
            """))
    elif NumRandom == 2:
        tiles.set_current_tilemap(tilemap("""
            level2
            """))
    elif NumRandom == 3:
        tiles.set_current_tilemap(tilemap("""
            level0
            """))
    else:
        tiles.set_current_tilemap(tilemap("""
            level3
            """))
    Render.set_view_mode(ViewMode.TILEMAP_VIEW)
    pause(2000)
    Render.set_view_mode(ViewMode.RAYCASTING_VIEW)
def level3():
    global NumRandom, level, mySprite
    NumRandom = randint(1, 4)
    level += 1
    sprites.destroy_all_sprites_of_kind(SpriteKind.thing2)
    Render.get_render_sprite_instance().set_kind(SpriteKind.player)
    mySprite = sprites.create(assets.image("""
        thing
        """), SpriteKind.thing3)
    tiles.place_on_tile(mySprite, tiles.get_tile_location(14, 14))
    scene.set_background_image(assets.image("""
        background
        """))
    tiles.place_on_tile(Render.get_render_sprite_instance(),
        tiles.get_tile_location(1, 1))
    if NumRandom == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
            """))
    elif NumRandom == 2:
        tiles.set_current_tilemap(tilemap("""
            level2
            """))
    elif NumRandom == 3:
        tiles.set_current_tilemap(tilemap("""
            level0
            """))
    else:
        tiles.set_current_tilemap(tilemap("""
            level3
            """))
    Render.set_view_mode(ViewMode.TILEMAP_VIEW)
    pause(2000)
    Render.set_view_mode(ViewMode.RAYCASTING_VIEW)
def level2():
    global NumRandom, level, mySprite
    NumRandom = randint(1, 4)
    level += 1
    sprites.destroy_all_sprites_of_kind(SpriteKind.thing)
    Render.get_render_sprite_instance().set_kind(SpriteKind.player)
    mySprite = sprites.create(assets.image("""
        thing
        """), SpriteKind.thing2)
    tiles.place_on_tile(mySprite, tiles.get_tile_location(14, 14))
    scene.set_background_image(assets.image("""
        background
        """))
    tiles.place_on_tile(Render.get_render_sprite_instance(),
        tiles.get_tile_location(1, 1))
    if NumRandom == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
            """))
    elif NumRandom == 2:
        tiles.set_current_tilemap(tilemap("""
            level2
            """))
    elif NumRandom == 3:
        tiles.set_current_tilemap(tilemap("""
            level0
            """))
    else:
        tiles.set_current_tilemap(tilemap("""
            level3
            """))
    Render.set_view_mode(ViewMode.TILEMAP_VIEW)
    pause(2000)
    Render.set_view_mode(ViewMode.RAYCASTING_VIEW)

def on_on_overlap(sprite, otherSprite):
    game.splash("You Win!, Level 3")
    level4()
sprites.on_overlap(SpriteKind.player, SpriteKind.thing3, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.splash("You Win!, Level 2")
    level3()
sprites.on_overlap(SpriteKind.player, SpriteKind.thing2, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    game.splash("You Win!, Level 1")
    level2()
sprites.on_overlap(SpriteKind.player, SpriteKind.thing, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    game.splash("You Win!, Level 4")
    game.game_over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.thing4, on_on_overlap4)

Ycoord = 0
Xcoord = 0
NumRandom = 0
mySprite: Sprite = None
level = 1
print("{\"text\":\"maze_started\"}")
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
    sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.player))
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO),
    sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.player))
sprites.destroy_all_sprites_of_kind(SpriteKind.thing)
Render.get_render_sprite_instance().set_kind(SpriteKind.player)
mySprite = sprites.create(assets.image("""
    thing
    """), SpriteKind.thing)
tiles.place_on_tile(mySprite, tiles.get_tile_location(14, 14))
scene.set_background_image(assets.image("""
    background
    """))
tiles.place_on_tile(Render.get_render_sprite_instance(),
    tiles.get_tile_location(1, 1))
tiles.set_current_tilemap(tilemap("""
    level1
    """))
Render.set_view_mode(ViewMode.RAYCASTING_VIEW)

def on_forever():
    global Xcoord
    Xcoord = int(Render.get_render_sprite_instance().x)
    console.log_value("X=", Xcoord)
forever(on_forever)

def on_forever2():
    global Ycoord
    Ycoord = int(Render.get_render_sprite_instance().y)
    console.log_value("Y=", Ycoord)
forever(on_forever2)

def on_forever3():
    console.log_value("Level", level)
forever(on_forever3)
