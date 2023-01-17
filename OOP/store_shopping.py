class Store:
    def __init__(self, address, name, stocked):
        self.__store_address = address
        self.__store_name = name
        self.__is_well_stocked = stocked

    def get_store_name(self):

        return self.__store_name

    def get_store_address(self):
        return self.__store_address

    def get_if_store_well_stocked(self):
        return self.__is_well_stocked