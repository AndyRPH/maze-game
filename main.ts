namespace SpriteKind {
    export const thing = SpriteKind.create()
    export const thing2 = SpriteKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    game.setDialogFrame(assets.image`frake1`)
    game.setDialogCursor(img`
        ............................7777
        ............................7777
        ............................7777
        ............................7777
        ..........................7777..
        ..........................7777..
        ..........................7777..
        ..........................7777..
        ........................777777..
        ........................777777..
        ........................7777....
        ........................7777....
        ......................777777....
        ......................777777....
        ......................7777......
        ......................7777......
        7777................777777......
        7777................777777......
        777777..............7777........
        777777..............7777........
        ..777777..........777777........
        ..777777..........777777........
        ....777777........7777..........
        ....777777........7777..........
        ......777777....777777..........
        ......777777....777777..........
        ........77777..77777............
        ........777777.77777............
        ..........7777777777............
        ..........7777777777............
        ............777777..............
        ............777777..............
        `)
    game.setDialogTextColor(10)
    game.showLongText("Maze Game V.1.9 \n Update Name: Pre-Launch By: Jacob \n Release Date: 7/14/2025", DialogLayout.Full)
})
function level2 () {
    random = randint(1, 9)
    level += 1
    sprites.destroyAllSpritesOfKind(SpriteKind.thing2)
    sprites.destroyAllSpritesOfKind(SpriteKind.thing)
    Render.getRenderSpriteInstance().setKind(SpriteKind.Player)
    mySprite = sprites.create(assets.image`thing`, SpriteKind.thing2)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(14, 14))
    scene.setBackgroundImage(assets.image`background`)
    tiles.placeOnTile(Render.getRenderSpriteInstance(), tiles.getTileLocation(1, 1))
    if (random == 1) {
        tiles.setCurrentTilemap(tilemap`Swirl`)
    } else if (random == 2) {
        tiles.setCurrentTilemap(tilemap`Enclosed Swirl`)
    } else if (random == 3) {
        tiles.setCurrentTilemap(tilemap`level7`)
    } else if (random == 4) {
        tiles.setCurrentTilemap(tilemap`level8`)
    } else if (random == 5) {
        tiles.setCurrentTilemap(tilemap`Ziggety Zaggety`)
    } else if (random == 6) {
        tiles.setCurrentTilemap(tilemap`Loops And Turns`)
    } else if (random == 7) {
        tiles.setCurrentTilemap(tilemap`Starter Maze`)
    } else if (random == 8) {
        tiles.setCurrentTilemap(tilemap`The Grid`)
    } else if (random == 9) {
        tiles.setCurrentTilemap(tilemap`level10`)
    } else {
    	
    }
    Render.setViewMode(ViewMode.tilemapView)
    pause(2000)
    Render.setViewMode(ViewMode.raycastingView)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.thing2, function (sprite, otherSprite) {
    game.splash("You Win This Level!!!!!")
    info.changeScoreBy(10)
    game.setGameOverEffect(true, effects.confetti)
    level2()
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    game.splash(game.askForString("Title creator", 24, true))
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.thing, function (sprite, otherSprite) {
    game.splash("You Win This Level!!!!!!")
    info.changeScoreBy(10)
    level2()
})
let Xcoord = 0
let Ycoord = 0
let random = 0
let mySprite: Sprite = null
let level = 1
console.log("{\"event\":\"maze_started\":\"true\"}")
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.One), sprites.create(img`
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
    `, SpriteKind.Player))
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two), sprites.create(img`
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
    `, SpriteKind.Player))
sprites.destroyAllSpritesOfKind(SpriteKind.thing)
Render.getRenderSpriteInstance().setKind(SpriteKind.Player)
mySprite = sprites.create(assets.image`thing`, SpriteKind.thing)
tiles.placeOnTile(mySprite, tiles.getTileLocation(14, 14))
scene.setBackgroundImage(assets.image`background`)
tiles.placeOnTile(Render.getRenderSpriteInstance(), tiles.getTileLocation(1, 1))
tiles.setCurrentTilemap(tilemap`Starter Maze`)
Render.setViewMode(ViewMode.raycastingView)
forever(function () {
    Ycoord = Math.trunc(Render.getRenderSpriteInstance().y)
    console.logValue("Y=", Ycoord)
    Xcoord = Math.trunc(Render.getRenderSpriteInstance().x)
    console.logValue("X=", Xcoord)
    console.logValue("Level", level)
})
