cimport libav as lib

from deepcodec.filter.context cimport FilterContext
from deepcodec.filter.filter cimport Filter
from deepcodec.filter.link cimport FilterLink


cdef class FilterPad:

    cdef readonly Filter filter
    cdef readonly FilterContext context
    cdef readonly bint is_input
    cdef readonly int index

    cdef const lib.AVFilterPad *base_ptr


cdef class FilterContextPad(FilterPad):

    cdef FilterLink _link


cdef tuple alloc_filter_pads(Filter, const lib.AVFilterPad *ptr, bint is_input, FilterContext context=?)
