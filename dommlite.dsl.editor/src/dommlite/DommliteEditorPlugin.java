package dommlite;

import org.openarchitectureware.xtext.AbstractXtextEditorPlugin;
import org.openarchitectureware.xtext.LanguageUtilities;
import org.osgi.framework.BundleContext;

public class DommliteEditorPlugin extends AbstractXtextEditorPlugin {
   private static DommliteEditorPlugin plugin;
   public static DommliteEditorPlugin getDefault() {
      return plugin;
   }

   private DommliteUtilities utilities = new DommliteUtilities();
   public LanguageUtilities getUtilities() {
      return utilities;
   }

   public DommliteEditorPlugin() {
      plugin = this;
   }

   public void stop(BundleContext context) throws Exception {
      super.stop(context);
      plugin = null;
   }
}
