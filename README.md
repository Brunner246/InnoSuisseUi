# InnoSuisseUi

## QDesigner

[Using .ui files from Designer](https://doc.qt.io/qtforpython-5/tutorials/basictutorial/uifiles.html)

### run
\Lib\site-packages\PySide2\designer.exe

### compile

use ``` pyside2-uic```

usage example ```pyside2-uic .\CInnosuisse.ui > .\GeneratedUi\Ui_CInnosuisse.py ```

## Translation

### create translation file

use ``` pyside2-lupdate```

usage example ```CInnosuisse.py -ts Translation_de.ts```

### compile translation file
use ``` pyside2-lrelease```

usage example ```lrelease Translation_de.ts```