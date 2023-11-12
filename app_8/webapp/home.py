import justpy as jp
from webapp import layout
from webapp import page


class Home(page.Page):

    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen')

        jp.Div(a=div, text='This is the Home page', classes='text-4xl m-2')
        jp.Div(a=div, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec mollis ut est faucibus malesuada. Nulla efficitur est nec luctus consequat. Sed finibus convallis nisi in efficitur. In sit amet mauris posuere, ullamcorper turpis a, scelerisque arcu. Aliquam dictum, felis id commodo maximus, arcu purus scelerisque augue, ut dignissim orci diam sit amet purus. Pellentesque efficitur hendrerit odio, molestie fermentum urna pharetra ac. Vestibulum eget turpis vel felis scelerisque cursus eget a massa. ', classes='text-lg')

        return wp
