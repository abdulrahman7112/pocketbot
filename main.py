from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from android.webview import WebView
from android.runnable import run_on_ui_thread

class WebViewLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        # شريط علوي بسيط
        self.top_bar = BoxLayout(size_hint_y=0.1)
        self.back_btn = Button(text='Back')
        self.back_btn.bind(on_press=self.go_back)
        self.top_bar.add_widget(self.back_btn)
        
        self.status_label = Label(text='Loading...')
        self.top_bar.add_widget(self.status_label)
        self.add_widget(self.top_bar)
        
        # واجهة WebView
        self.webview = WebView()
        self.add_widget(self.webview)
        
        # تحميل موقع Pocket Option
        Clock.schedule_once(lambda dt: self.load_website(), 1)
    
    @run_on_ui_thread
    def load_website(self):
        self.webview.loadUrl('https://pocketoption.com/ar/cabinet/demo-quick-high-low/')
    
    @run_on_ui_thread
    def go_back(self, instance):
        if self.webview.canGoBack():
            self.webview.goBack()

class PocketBotApp(App):
    def build(self):
        return WebViewLayout()

if __name__ == '__main__':
    PocketBotApp().run()
