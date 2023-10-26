using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Alpaca4d.Core.Template
{
    public class MomentCurvature2
    {
        public static string Define()
        {
            // initialize MomentCurvature tcl file
            StringBuilder MKtcl = new StringBuilder();

            // Set up
            MKtcl.Comment(" SET UP ----------------------------------------");
            MKtcl.Code("wipe");

            return MKtcl.ToString();
        }


    }

    public static class StringBuilderExtensions
    {
        public static StringBuilder Comment(this StringBuilder stringBuilder, string comment)
        {
            stringBuilder.Append("# " + comment + " \n");
            return stringBuilder;
        }

        public static StringBuilder Code(this StringBuilder stringBuilder, string code)
        {
            stringBuilder.Append(code + ";\n");
            return stringBuilder;
        }
    }
}

