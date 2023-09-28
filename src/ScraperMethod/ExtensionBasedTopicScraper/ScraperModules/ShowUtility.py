import os

from src.Logging.Logger import Logger
from src.Utility.FileUtility import FileUtility


class ShowUtility:
    def __init__(self, configJson):
        self.browser = None
        self.fileUtils = FileUtility()
        selectorPath = os.path.join(os.path.dirname(__file__), "Selectors.json")
        self.selectors = self.fileUtils.loadJsonFile(selectorPath)["ShowUtility"]
        self.logger = Logger(configJson, "ShowUtility").logger


    def showSingleMarkDownQuizSolution(self):
        try:
            self.logger.info("Showing single markdown quiz solution")
            showMarkDownQuizSolutionSelector = self.selectors["showMarkDownQuizSolution"]
            showMarkDownQuizJsScript = f"""
            var divs = document.querySelectorAll('div');
            var count = 0;
            divs.forEach(div => {{
              if (div.textContent.trim() === "{showMarkDownQuizSolutionSelector}") {{
                  div.click();
                  count++;
              }}}});
            return count;
            """
            isPresent = self.browser.execute_script(showMarkDownQuizJsScript)
            if isPresent <= 0:
                self.logger.info("No single markdown quiz solution found")
        except Exception as e:
            lineNumber = e.__traceback__.tb_lineno
            raise Exception(f"ShowUtility:showSingleMarkDownQuizSolution: {lineNumber}: {e}")


    def showCodeSolutions(self):
        try:
            self.logger.info("Showing code solutions")
            showCodeSolutionSelector = self.selectors["showCodeSolution"]
            confirmButtonSelector = self.selectors["confirmShowSolution"]
            showCodeSolutionJsScript = f"""
            var buttons = document.querySelectorAll('button');
            var count = 0;
            buttons.forEach(button => {{
              if (button.textContent.trim() === "{showCodeSolutionSelector}" && button.disabled === false) {{
                  button.click();
                  document.querySelector("{confirmButtonSelector}").click();
                  button.disabled = true;
                  count++;
            }}}});
            return count;
            """
            isPresent = self.browser.execute_script(showCodeSolutionJsScript)
            if isPresent <= 0:
                self.logger.info("No code solution found")
        except Exception as e:
            lineNumber = e.__traceback__.tb_lineno
            raise Exception(f"ShowUtility:showCodeSolutions: {lineNumber}: {e}")


    def showHints(self):
        try:
            self.logger.info("Showing hints")
            showHintSelector = self.selectors["showHints"]
            showHintJsScript = f"""
            var gs = document.querySelectorAll("{showHintSelector}");
            var count = 0;
            gs.forEach(g => {{
                var button = g.closest('svg').parentNode;
                if(button.disabled === false) {{
                  button.click();
                  button.disabled = true;
                  count++;
            }}}});
            return count;
            """
            isPresent = self.browser.execute_script(showHintJsScript)
            if isPresent <= 0:
                self.logger.info("No hints found")
        except Exception as e:
            lineNumber = e.__traceback__.tb_lineno
            raise Exception(f"ShowUtility:showHints: {lineNumber}: {e}")


    def showSlides(self):
        try:
            self.logger.info("Showing slides")
            showSlideSelector = self.selectors["showSlides"]
            showSlideJsScript = f"""
            var svgs = document.querySelectorAll("{showSlideSelector}");
            var count = 0;
            svgs.forEach(svg => {{
                var button = svg.parentNode;
                if(button.disabled === false) {{
                  button.click();
                  button.disabled = true;
                  count++;
            }}}});
            return count;
            """
            isPresent = self.browser.execute_script(showSlideJsScript)
            if isPresent <= 0:
                self.logger.info("No slides found")
        except Exception as e:
            lineNumber = e.__traceback__.tb_lineno
            raise Exception(f"ShowUtility:showSlides: {lineNumber}: {e}")