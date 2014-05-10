
    //  memcached 采用 slab 的内存管理方法.
    slabs_free(it, ntotal, clsid);
}
bool item_size_ok(const size_t nkey, const int flags, const int nbytes) {
    char prefix[40];
    uint8_t nsuffix;

    size_t ntotal = item_make_header(nkey + 1, flags, nbytes,
