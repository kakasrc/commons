package simple.server;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.webapp.WebAppContext;

public class WebAppWithSource
{
    public static void main(String[] args) throws Exception
    {
        Server server = new Server(8080);
 
        WebAppContext context = new WebAppContext();
        context.setDefaultsDescriptor("./demo-kaka/web.xml");
        context.setResourceBase("./demo-kaka/");
        context.setContextPath("/");
        context.setParentLoaderPriority(true);
 
        server.setHandler(context);
 
        server.start();
        server.join();
    }
}
