import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform
from kivy.clock import Clock

# অ্যান্ড্রয়েড স্পেসিফিক স্টোরেজ ও ফাইল সিলেক্টর মডিউল
if platform == 'android':
    from android.storage import primary_external_storage_path
    from android.permissions import request_permissions, Permission
    from plyer import filechooser

class RuMediaMain(BoxLayout):
    def __init__(self, **kwargs):
        super(RuMediaMain, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20
        
        self.selected_file = None
        self.storage_path = ""

        # টাইটেল
        self.add_widget(Label(
            text="RuMedia Master Pro", 
            font_size='28sp', 
            bold=True, 
            color=(0.2, 0.6, 1, 1),
            size_hint_y=0.2
        ))

        # স্ট্যাটাস স্ক্রিন
        self.status_label = Label(
            text="No file selected\nInitializing Storage...", 
            halign='center',
            size_hint_y=0.4
        )
        self.add_widget(self.status_label)

        # অ্যাড মিডিয়া বাটন (যা গ্যালারি ওপেন করবে)
        self.add_btn = Button(
            text="[ + ] Add Media", 
            size_hint_y=0.2,
            background_color=(0.1, 0.2, 0.4, 1)
        )
        self.add_btn.bind(on_press=self.open_gallery)
        self.add_widget(self.add_btn)

        # স্টার্ট বাটন
        self.start_btn = Button(
            text="Start Unikalize", 
            size_hint_y=0.2,
            background_color=(0.05, 0.3, 0.1, 1)
        )
        self.add_widget(self.start_btn)

        # অ্যাপ চালু হলেই পারমিশন চাওয়া এবং ফোল্ডার তৈরি করা
        if platform == 'android':
            request_permissions([
                Permission.READ_EXTERNAL_STORAGE, 
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.MANAGE_EXTERNAL_STORAGE
            ], self.create_auto_folder)
        else:
            Clock.schedule_once(self.create_auto_folder, 1)

    def create_auto_folder(self, *args):
        # ফোন মেমোরিতে অটোমেটিক ফোল্ডার ক্রিয়েশন লজিক
        if platform == 'android':
            primary_path = primary_external_storage_path()
            self.storage_path = os.path.join(primary_path, "RuMediaMaster")
        else:
            self.storage_path = os.path.join(os.path.expanduser("~"), "RuMediaMaster")

        try:
            if not os.path.exists(self.storage_path):
                os.makedirs(self.storage_path)
            self.status_label.text = f"No file selected\nOutput Folder: {self.storage_path}"
        except Exception as e:
            self.status_label.text = f"Storage Error: {str(e)}"

    def open_gallery(self, instance):
        # ডিরেক্ট ফোন মেমোরি/গ্যালারির সব ভিডিও ফাইল ওপেন করার লজিক
        try:
            if platform == 'android':
                filechooser.open_file(
                    on_selection=self.handle_selection, 
                    filters=[("Video Files", "*.mp4", "*.mkv", "*.avi", "*.3gp")]
                )
            else:
                filechooser.open_file(on_selection=self.handle_selection)
        except Exception as e:
            self.status_label.text = f"Gallery Error: {str(e)}"

    def handle_selection(self, selection):
        if selection:
            self.selected_file = selection[0]
            filename = os.path.basename(self.selected_file)
            self.status_label.text = f"Selected Video: {filename}\nReady to Unikalize!"
        else:
            self.status_label.text = "No file selected."

class RuMediaApp(App):
    def build(self):
        return RuMediaMain()

if __name__ == '__main__':
    RuMediaApp().run()
