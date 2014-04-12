
package dommlite.parser;

import java.io.InputStream;

import org.openarchitectureware.expression.ExecutionContext;
import org.openarchitectureware.workflow.util.ResourceLoader;
import org.openarchitectureware.workflow.util.ResourceLoaderFactory;
import org.openarchitectureware.workflow.util.ResourceLoaderImpl;
import org.openarchitectureware.xtend.XtendFacade;
import org.openarchitectureware.xtext.parser.ErrorMsg;

public class XtextParser extends GenParser {

	@Override
	protected void internalPreLink() {
		ResourceLoader cl = ResourceLoaderFactory.createResourceLoader();
		try {
			ResourceLoaderFactory.setCurrentThreadResourceLoader(new ResourceLoaderImpl(XtextParser.class.getClassLoader()));
			ExecutionContext ctx = getExecutionContext();
			XtendFacade facade = XtendFacade.create(ctx, "dommlite::Extensions");
			facade.call("injectBuildIns", getRootNode().getModelElement());
		} catch (Exception e) {
			internalErrors.add(new ErrorMsg("Error during creating buildin types: "+e.getMessage(),0,1,1));
		} finally {
			ResourceLoaderFactory.setCurrentThreadResourceLoader(cl);
		}
		
	}

	public XtextParser(InputStream in) {
		super(in);
	}

}
