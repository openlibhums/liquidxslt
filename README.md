# liquidxslt

The liquidxslt plugin lets you edit existing XSL stylesheet and generate new XSL stylesheets based on existing versions. When creating an XSL template the default content will have an import statement for the existing stylesheet. Using `<xsl: import>` over `<xsl: include>` means that you can easily override matches as the importing sheet has higher presendence than the imported sheet.


## example
The follwing stylesheet is based on the 1.4 default XSL file.
```
<xsl:stylesheet version="1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:tei="http://www.tei-c.org/ns/1.0"
                exclude-result-prefixes="xsi xs xlink mml">
    <xsl:import href="/path/to/janeway/src/files/xsl/default-v1.4.xsl"/>
</xsl:stylesheet>
```
