from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.webview import WebView


class WebPageViewer(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Label to display instructions or information
        info_label = Label(text="Webpage Viewer", size_hint=(1, 0.1))
        layout.add_widget(info_label)

        # WebView to display the webpage
        webview = WebView(url="https://192.168.0.103", size_hint=(1, 0.9))
        layout.add_widget(webview)

        return layout


if __name__ == '__main__':
    WebPageViewer().run()

