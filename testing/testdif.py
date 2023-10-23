import difPy

if __name__ == "__main__":
    dif = difPy.build('./tmp_images/AAselected/')
    search = difPy.search(dif)
    print(search.result)