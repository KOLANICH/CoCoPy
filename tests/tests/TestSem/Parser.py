__copyright__ = """
If not otherwise stated, any source code generated by Coco/R (other than Coco/R itself) does not fall under the GNU General Public License.
"""
import typing
from functools import wraps
import sys
from CoCoRuntime.parser import Parser
from CoCoRuntime.scanner import Position
from .Scanner import ScannerEnum


def _generateSet() -> typing.Tuple[typing.Tuple[bool, ...], ...]:
	T = True
	x = False
	return ((T, x, x, x, x, x, x, x, x, x, x),)


class MyParser(Parser):
	__slots__ = ()

	@wraps(Parser.__init__)
	def __init__(self, *args, **kwargs):
		"""This ctor is mandatory, don't delete it: otherwise self.__class__.ENUM will be None"""
		super().__init__(*args, **kwargs)

	ENUM = ScannerEnum
	__main_production_name__ = "Test"
	__EOF_sym__ = ScannerEnum.EOF_SYM

	def Foo():
		sys.stdout.write("foo\n")

	def pragmas(self) -> None:
		if self.la.kind == self.__class__.ENUM.option_Sym:
			sys.stdout.write("pragma\n")

	def Test(self) -> None:
		decl
		self.A()
		self.B()
		self.C()

	def A(self) -> None:
		if self.la.kind == self.__class__.ENUM.c_Sym:
			aaa
			self.Get()
		elif self.la.kind == self.__class__.ENUM.a_Sym or self.la.kind == self.__class__.ENUM.b_Sym:
			bbb
		elif self.la.kind == self.__class__.ENUM.d_Sym:
			self.Get()
		else:
			self.SynErr(11)
		ccc

	def B(self) -> None:
		ddd
		while self.la.kind == self.__class__.ENUM.a_Sym:
			self.Get()
			eee
		fff
		self.Expect(self.__class__.ENUM.b_Sym)
		m = lambda a, x: a @ x + b * int(c) % d ^ e & f

	def C(self) -> None:
		if self.la.kind == self.__class__.ENUM.a_Sym:
			self.Get()
		elif self.la.kind == self.__class__.ENUM.b_Sym:
			self.Get()
		else:
			self.SynErr(12)
		ggg
		self.Expect(self.__class__.ENUM.c_Sym)

	set = _generateSet()
	errorMessages = "EOF expected", "a expected", "b expected", "c expected", "d expected", "e expected", "f expected", "g expected", "h expected", "i expected", "??? expected", "invalid A", "invalid C"
