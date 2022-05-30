import os

from controlers.app import GameOfLiveApp


def main_app():
    app = GameOfLiveApp()
    app.run()


if __name__ == '__main__':
    os.environ["SDL_VIDEO_CENTERED"] = '1'
    main_app()
