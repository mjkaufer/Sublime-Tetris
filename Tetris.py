import sublime
import sublime_plugin
import random
import copy


class AnimateCommand(sublime_plugin.TextCommand):
    lastGrid = None

    rows = 20 + 2#2 represents the borders
    cols = 10 + 2

    def run(self, edit):

        totalRegion = sublime.Region(0, self.view.size())
        if not self.lastGrid:
            self.lastGrid = []

            for r in range(self.rows):

                self.lastGrid.append([])

                for c in range(self.cols):
                    char = " "
                    if c == 0 or c == self.cols - 1:
                        if r == 0 or r == self.rows - 1:
                            char = "+"
                        else:
                            char = "|"
                    elif r == 0 or r == self.rows - 1:
                        char = "-"

                    self.lastGrid[r].append(char)

        self.nextFrame(self.lastGrid)

        newContents = ""

        for r in range(len(self.lastGrid)):
            for c in range(len(self.lastGrid[r])):
                newContents += self.lastGrid[r][c]
            newContents += "\n"

        # to get rid of trailing newline
        newContents = newContents[:len(newContents) - 1]

        self.view.replace(edit, totalRegion, newContents)

    def nextFrame(self, grid):

        changes = {}

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                    # changes[(r, c)] = " "
                break

        for coord in changes:
            r = coord[0]
            c = coord[1]
            grid[r][c] = changes[coord]

        return grid


class TetrisCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print("A")

        boardView = sublime.active_window().new_file()
        boardView.set_name("Tetris")
        # boardView.set_read_only(True)

        boardView.run_command("animate")


    # def animate(self, boardView):
    #     # if not self.running:
    #     #     self.running = False
    #     #     return

    #     # firstTime = x == 0

    #     boardView.run_command("animate")

    #     # if self.running:
    #     #     sublime.set_timeout(lambda: self.animate(1), 100)
