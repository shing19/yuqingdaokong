# 检索分为两类：支持（support）和调停（mediate）
from config import get_dict


class Input:
    def __init__(self, text, target, scene, label):
        _, self.text = self.data_validator('text', text)
        _, self.target = self.data_validator('target', target)
        _, self.scene = self.data_validator('scene', scene)
        _, self.label = self.data_validator('label', label)
        
        
    def data_validator(self, param_type, data):
        validation_result = False
        input_result = None
        if param_type == 'text':
            try:
                data = data.strip()
                validation_result = True if (len(data) != 0) else False
                input_result = data if (len(data) != 0) else None
            except:
                return False, None
        if param_type == 'target':
            try:
                data = eval(data)
                validation_result = True if (data == 0 or data == 1) else False
                input_result = data if (data == 0 or data == 1) else None
            except:
                return False, None
        if param_type == 'scene' or param_type == 'label':
            try:
                data = data.strip()
                dict_list = get_dict(param_type)
                validation_result = True if (data in dict_list) else False
                input_result = data if (data in dict_list) else None
            except:
                return False, None
        return validation_result, input_result
        
        
    def query_input(self, param_type, input_tips):
        while True:
            data = input(input_tips)
            validation_result, input_result = self.data_validator(self, param_type, data)
            if validation_result:
                return input_result
            else:
                print('输入错误，请重新输入！')

                
    @classmethod
    def from_input(cls):
        text = cls.query_input(cls, 'text', '请输入目标内容: ')
        target = cls.query_input(cls, 'target', '请输入检索目的（1-支持 0-调停）: ')
        scene = cls.query_input(cls, 'scene', '请输入帖子场景: ')
        label = cls.query_input(cls, 'label', '请输入回复类型: ')
        return cls(
            text, 
            target,
            scene,
            label,
        )
    
    
    def __str__(self):
        target = '支持' if self.target == 1 else '调停'
        return f'目标为“{target}”，将在“{self.scene}”场景和“{self.label}”回复类型中搜索“{self.text}”'
    
        

if __name__ == '__main__':
    input = Input.from_input()
#     test = Input('好耶', '1', '异常说明公告', '期待祝福许愿')
    print(input)