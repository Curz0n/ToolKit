package com.xposed.hooks.xposedmodules;

import android.util.Log;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.callbacks.XC_LoadPackage;

/**
 * Created by Curz0n on 2017/5/19.
 */

public class XposedHookLoadPackageEntry implements IXposedHookLoadPackage{

    private static final String TAG = "Hook";
    //TODO:Replace target package name here.
    private static final String packageName = "";

    @Override
    public void handleLoadPackage(XC_LoadPackage.LoadPackageParam loadPackageParam) throws Throwable {
        //Log.d(TAG,"================test=================");

        if(loadPackageParam.packageName.equals(packageName)){
            Log.d(TAG,"==================HOOK SUCCESS===============");
        }


        XposedHelpers.findAndHookMethod("android.app.Application", loadPackageParam.classLoader, "method", String.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                super.beforeHookedMethod(param);
            }

            @Override
            protected void afterHookedMethod(MethodHookParam param) throws Throwable {
                super.afterHookedMethod(param);
            }
        });


    }
}
