# TV 클래스와 생성자
# 생성자 키워드 : __init__
# 생성자에는 'self'라는 키워드를 사용하여 내부의 값을 초기화 합니다. (필수)
class TV :
    def __init__ (self, name, is_on, channel, volume) :
        self.name = name
        self.is_on = is_on
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on) :
        self.is_on = is_on
    def set_channel(self, channel) :
        self.channel = channel
    def set_volume(self, volume) :
        self.volume = volume
    def get_on(self) :
        return self.is_on
    def get_channel(self) :
        return self.channel
    def get_volume(self) :
        return self.volume
    def view_tv(self) :
        power = "OFF", "ON"
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.is_on]}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")
    

lg_tv = TV('LG', False, 7, 10)
samsung_tv = TV('Samsung', False, 11, 5)

lg_tv.view_tv()
print('-'*20)
samsung_tv.view_tv()