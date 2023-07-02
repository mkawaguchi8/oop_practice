class User:
    def __init__(self, name):
       if not (4 <= len(name) <= 20):
           raise ValueError(f"{name}はルール違反です")     
       self.name = name

# screen_nameメソッドの作成
    def screen_name(self):
        # upperは大文字に変換する
        return self.name.upper()

# self_introctionメソッドの作成    
    def self_introduction(self):
        return f"私の名前は{self.name.upper()}です"
       

# Userクラスのインスタント化
tanaka = User(name='tanaka')

# 出力
print(tanaka.screen_name())
print(tanaka.self_introduction())
