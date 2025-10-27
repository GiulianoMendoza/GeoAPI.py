class TitleUnique:
    def exists_title(self, title:str) ->bool: #self = this ref instacia actual 
        raise NotImplementedError

def ensure_unique_title(checker: TitleUnique, title:str) -> None:
    if checker.exists_title(title):
        raise ValueError("title already exists")