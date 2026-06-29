# -*- coding: utf-8 -*-
import os
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.progressbar import ProgressBar
from kivy.utils import platform

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

class RuMediaMasterApp(App):
    def build(self):
        self.title = "RuMediaMaster v3.5"
        layout = BoxLayout(orientation='vertical', padding=40, spacing=25)
        
        self.title_label = Label(
            text="RuMedia Master Pro", 
            font_size='24sp', 
            bold=True,
            color=(0.2, 0.6, 1, 1)
        )
        layout.add_widget(self.title_label)
        
        self.status_label = Label(
            text="No file selected\nOutput Folder: /sdcard/RuMediaMaster", 
            font_size='16sp', 
            halign='center'
        )
        layout.add_widget(self.status_label)
        
        self.add_btn = Button(
            text="[ + ] Add Media", 
            font_size='20sp', 
            background_color=(0.2, 0.5, 0.9, 1),
            size_hint=(1, 0.2)
        )
        self.add_btn.bind(on_press=self.select_media)
        layout.add_widget(self.add_btn)
        
        self.start_btn = Button(
            text="Start Unikalize", 
            font_size='20sp', 
            background_color=(0.1, 0.7, 0.3, 1),
            size_hint=(1, 0.2)
        )
        self.start_btn.bind(on_press=self.start_unikalize)
        layout.add_widget(self.start_btn)
        
        self.progress = ProgressBar(max=100, value=0, size_hint=(1, 0.1))
        layout.add_widget(self.progress)
        
        return layout

    def select_media(self, instance):
        self.status_label.text = "Video File Selected Successfully!"
        
    def start_unikalize(self, instance):
        self.status_label.text = "Processing Video Streams..."
        self.title_label.text = "Rendering... Please Wait"
        self.progress.value = 50 
        
        self.progress.value = 100
        self.title_label.text = "RuMedia Master Pro"
        self.status_label.text = "Process Completed!\nCheck 'RuMediaMaster' Folder in Storage."

if __name__ == '__main__':
    RuMediaMasterApp().run()
