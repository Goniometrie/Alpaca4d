using System;
using System.Collections.Generic;

using Grasshopper.Kernel;
using Rhino.Geometry;

namespace Alpaca4d.Gh._11_MomentCurvature
{
    public class MomentCurvature2 : GH_Component
    {
        /// <summary>
        /// Initializes a new instance of the MomentCurvature2 class.
        /// </summary>
        public MomentCurvature2()
          : base("MomentCurvature2", "MomentCurvature2",
              "Description",
              "Alpaca4d", "MomentCurvature")
        {
        }

        /// <summary>
        /// Registers all the input parameters for this component.
        /// </summary>
        protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager)
        {
            pManager.AddBooleanParameter("run", "run", "run script", GH_ParamAccess.item);
        }

        /// <summary>
        /// Registers all the output parameters for this component.
        /// </summary>
        protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager)
        {
        }

        /// <summary>
        /// This is the method that actually does the work.
        /// </summary>
        /// <param name="DA">The DA object is used to retrieve from inputs and store in outputs.</param>
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            bool run = false;
            //string dir = "y";
            DA.GetData(0, ref run);

            if (run) 
            {
                string text = "0"; 
            }
        }

        /// <summary>
        /// Provides an Icon for the component.
        /// </summary>
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                //You can add image files to your project resources and access them like this:
                // return Resources.IconForThisComponent;
                return null;
            }
        }

        /// <summary>
        /// Gets the unique ID for this component. Do not change this ID after release.
        /// </summary>
        public override Guid ComponentGuid
        {
            get { return new Guid("0C69C090-E50D-49C6-AC39-4D7D5E121544"); }
        }
    }
}