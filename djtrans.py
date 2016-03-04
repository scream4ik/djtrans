import sublime_plugin


class DjtransCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                s = self.view.substr(region)
                self.view.replace(edit, region, "{% trans '" + s + "' %}")
