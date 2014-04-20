"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment


class DisqusXBlock(XBlock):
    """
    This XBlock will embed a Disqus forum.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    shortname = String(
           scope = Scope.settings, 
           help = "URL for MP3 file to play",
           default = 'edx'
        )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the DisqusXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/disqus.html")
        extras = '';
        frag = Fragment(html.replace('SHORTNAME','makerphysics').replace('EXTRAS',extras))
        frag.add_css(self.resource_string("static/css/disqus.css"))
        frag.add_javascript(self.resource_string("static/js/src/disqus.js"))
        frag.initialize_js('DisqusXBlock')
        print self.xml_text_content()
        return frag

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("DisqusXBlock",
             """<vertical_demo>
                  <disqus src="http://localhost/Ikea.mp3"> </disqus>
                  <disqus src="http://localhost/skull.mp3"> </disqus>
                  <disqus src="http://localhost/monkey.mp3"> </disqus>
                </vertical_demo>
             """),
        ]
