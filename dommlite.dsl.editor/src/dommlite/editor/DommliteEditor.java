package dommlite.editor;

import org.openarchitectureware.xtext.AbstractXtextEditorPlugin;
import org.openarchitectureware.xtext.editor.AbstractXtextEditor;

import dommlite.DommliteEditorPlugin;

public class DommliteEditor extends AbstractXtextEditor {

   public AbstractXtextEditorPlugin getPlugin() {
      return DommliteEditorPlugin.getDefault();
   }
}
